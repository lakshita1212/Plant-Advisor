# Spec: `run_agent()`

**File:** `agent.py`
**Status:** Partially pre-filled — complete the two blank fields before implementing

---

## Purpose

Orchestrate a single conversational turn for the Plant Advisor agent. Given a user message and the conversation history, call the LLM with available tools, execute any tool calls the LLM requests, and return the final text response.

This is the core of what makes Plant Advisor an *agent* rather than a simple chatbot: the ability to decide which tools to call, use their results to inform its response, and loop until it has everything it needs.

---

## Input / Output Contract

**Inputs:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `user_message` | `str` | The user's current message |
| `history` | `list` | Gradio conversation history — list of `{"role": ..., "content": ...}` message dicts |

**Output:** `str`

The agent's final text response for this turn. Should never be empty — if something goes wrong, return a user-readable fallback message.

---

## Design Decisions

*Read `specs/system-design.md` (especially the "How the Groq Tool Calling API Works" section) before reviewing these. Complete the two blank fields before writing any code.*

---

### Messages list structure

The messages list must start with the system prompt, then replay the conversation
history, then add the new user message. The app creates its chat UI with
`type="messages"`, so Gradio history arrives as a list of API-format dicts with
`role` and `content` keys. Gradio may include extra keys (like `metadata`), so
copy only the two fields the API expects:

```python
messages = [{"role": "system", "content": SYSTEM_PROMPT}]

for msg in history:
    messages.append({"role": msg["role"], "content": msg["content"]})

messages.append({"role": "user", "content": user_message})
```

---

### Initial LLM call

Pass the model, the messages list, the tool definitions, and `tool_choice="auto"`
so the LLM can decide whether to call a tool or respond directly:

```python
response = client.chat.completions.create(
    model=LLM_MODEL,
    messages=messages,
    tools=TOOL_DEFINITIONS,
    tool_choice="auto",
)
```

---

### Detecting tool calls in the response

The response object has a `choices` list. Index 0 gives the assistant message.
Check its `tool_calls` attribute — if it's truthy, the LLM wants to call tools:

```python
assistant_message = response.choices[0].message

if not assistant_message.tool_calls:
    # No tool calls — LLM has a final answer
    ...
```

---

### Appending the assistant message

When there are tool calls, append the full assistant message object to `messages`
**before** appending any tool results. The API requires this ordering — a tool
result message must immediately follow the assistant message that requested it:

```python
messages.append(assistant_message)  # must come first
```

---

### Executing and appending tool results

For each tool call, extract the name and arguments, call `dispatch_tool()`, and
append the result as a `"tool"` role message. The `tool_call_id` links this result
back to the specific tool call that requested it.

⚠️ For a no-argument tool call (like `get_seasonal_conditions` with no season),
the model may send `arguments` as the JSON string `"null"` — `json.loads` turns
that into `None`, not `{}`. Normalize before dispatching:

```python
for tool_call in assistant_message.tool_calls:
    tool_name = tool_call.function.name
    raw_args = tool_call.function.arguments
    tool_args = json.loads(raw_args) if raw_args else {}
    if not isinstance(tool_args, dict):
        tool_args = {}
    tool_result = dispatch_tool(tool_name, tool_args)

    messages.append({
        "role": "tool",
        "tool_call_id": tool_call.id,
        "content": tool_result,
    })
```

---

### Loop termination conditions

*The loop should stop when: (a) the LLM returns a response with no tool calls, OR (b) the MAX_TOOL_ROUNDS limit is reached. Describe how you will detect each condition and what you will return in each case.*

```
To safely control the agent loop, I will track iterations using a counter variable (e.g., `current_round = 0`) initialized right before the loop starts. Inside a `while True:` block, the loop will evaluate two distinct exit criteria:

1. Condition A: Success (No Tool Calls)
   - How to detect: After fetching the `assistant_message = response.choices[0].message`, inspect the `tool_calls` attribute. If `not assistant_message.tool_calls` evaluates to True, it means the LLM is done gathering data and has formulated its final answer.
   - What to return: Break the loop and return the extracted final text content from this response.

2. Condition B: Safety Valve (MAX_TOOL_ROUNDS Reached)
   - How to detect: At the end of each iteration where tools were successfully dispatched and appended, increment the counter (`current_round += 1`). Check if `current_round >= MAX_TOOL_ROUNDS`.
   - What to return: If this threshold is hit, break the loop immediately to prevent an infinite API loop. Return a clean, user-friendly fallback string such as: "I've gathered as much information as possible, but I hit my search limit. Based on what I know..." or a standard error handler fallback if no text content was generated.
```

---

### Extracting the final text response

*Once the loop exits because there are no more tool calls, how do you extract the text content from the response object? What field holds the string you should return?*

```
When the loop determines that `assistant_message.tool_calls` is empty or None, the final text response string resides inside the message's content property.

- Exact path: `response.choices[0].message.content`
- Access logic: I will grab `final_text = assistant_message.content`. Before returning, I will check if `final_text` is valid and not empty. If for some reason it is empty or None (e.g., a parsing anomaly), I will return a graceful fallback string to ensure the user always sees a readable answer.
```

---

## Implementation Notes

*Fill this in after implementing and testing.*

**Trace of a working agent turn (what tools were called and in what order):**

```
Query: "How should I care for my calathea?"
Round 1 tool call: [tool name, args]
Round 2 tool call: [tool name, args] (if any)
Final response: [brief description]
```

**What happens when you ask about a plant that isn't in the database?**

```
[describe the behavior you observed]
```

**One thing about the tool call API that surprised you:**

```
[your answer here]
```
