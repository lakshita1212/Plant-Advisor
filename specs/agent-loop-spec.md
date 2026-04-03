# Spec: `run_agent()`

**File:** `agent.py`
**Status:** Spec incomplete — fill in all blank fields before implementing

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
| `history` | `list` | Gradio conversation history — list of `[user_msg, assistant_msg]` pairs |

**Output:** `str`

The agent's final text response for this turn. Should never be empty — if something goes wrong, return a user-readable fallback message.

---

## Design Decisions

*Complete all fields below before writing any code. Read `specs/system-design.md` (especially the "How the Groq Tool Calling API Works" section) before filling these in. Use Plan or Ask mode to work through the parts that are unclear.*

---

### Messages list structure

*Describe the full structure of the messages list at the start of the function, before any LLM calls. What goes in it, in what order? Include the format of history messages.*

```
[your answer here]
```

---

### Initial LLM call

*What arguments do you pass to `client.chat.completions.create()` for the first call? List the key parameters and their values.*

```
[your answer here]
```

---

### Detecting tool calls in the response

*How do you check whether the LLM's response contains tool calls? What field do you inspect?*

```
[your answer here]
```

---

### Appending the assistant message

*When there are tool calls, you must append the assistant message before appending tool results. What does that append look like? Why does order matter?*

```
[your answer here]
```

---

### Executing and appending tool results

*For each tool call: how do you get the tool name and arguments? How do you call dispatch_tool()? What does the tool result message look like?*

```
[your answer here]
```

---

### Loop termination conditions

*The loop should stop when: (a) the LLM returns a response with no tool calls, OR (b) the MAX_TOOL_ROUNDS limit is reached. Describe how you'll detect each condition and what you return in each case.*

```
[your answer here]
```

---

### Extracting the final text response

*Once the loop exits normally (no more tool calls), how do you extract the text content from the response object to return as a string?*

```
[your answer here]
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
