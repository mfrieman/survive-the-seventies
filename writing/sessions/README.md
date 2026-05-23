# Sessions Archive

Persistent record of every meaningful Clawpilot conversation about this project. The chat-history equivalent of git commits.

## Why this exists

The Clawpilot AI assistant stores session transcripts and memories in a local SQLite database (`~/.copilot/session-store.db`) that's tied to the install. If the subscription ends, the install breaks, or the disk dies, **the reasoning behind the project's creative decisions could be lost** — only the canon docs (`premise.md`, `world.md`, etc.) would survive.

This folder ensures every conversation is exported to git-tracked Markdown so:

1. **The full reasoning is preserved forever** in the GitHub repo.
2. **A new AI assistant can ingest the history** and pick up exactly where we left off.
3. **The project is independent of any single AI tool** — Clawpilot, ChatGPT, Claude, whatever comes next.

## How to use

### Export current session

After any meaningful conversation, ask Clawpilot:

> "checkpoint" — exports the current session, updates `decisions-log.md`, updates relevant canon docs

Or manually:

```powershell
# Find the current session ID (look in Clawpilot UI or session-state folder)
node --experimental-sqlite writing/sessions/export_session.mjs <session-id> writing/sessions/<YYYY-MM-DD_topic>.md
```

### Naming convention

`YYYY-MM-DD_topic.md` — e.g. `2026-05-22_romance-arc-iwona.md`

For multi-day sessions: `YYYY-MM-DD_YYYY-MM-DD_topic.md`

## What's in each export

- Session metadata (created, updated, working dir, repo)
- Checkpoint summaries (if any)
- Files touched during the session
- Full turn-by-turn transcript with timestamps

The transcript is rendered as fenced code blocks so any markdown inside the conversation doesn't pollute rendering.

## Requirements

- Node.js 22+ (uses built-in `node:sqlite` with `--experimental-sqlite` flag)
- Read access to `~/.copilot/session-store.db`

## Onboarding a new AI assistant

Tell the new assistant:

> "Read `writing/premise.md` and `writing/decisions-log.md` first. Then skim the most recent file in `writing/sessions/`. The canon docs are the source of truth; the session archive is the reasoning trail."

That should bring any capable LLM up to speed in about 10 minutes.
