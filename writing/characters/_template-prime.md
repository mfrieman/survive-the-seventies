# [NN] — [Character Name] · PRIME (Tier 3)

> **Status:** [DRAFT / CANON] · **Tier 3 (Prime)** — fork-measured, full relationship.
> **One-line essence:** [who they are in a sentence].
> **Gates:** [parts / muster / info — what befriending them unlocks].
> **Note thread type:** [🔧 Part · 👥 Muster · ✉️ Mentor/Story].

---

## 1. Personality

- **Want / Wound / Lie:**
  - *Wants:* [surface goal]
  - *Wound:* [the hurt underneath]
  - *Lie they believe:* [the self-deception that drives them]
- **Voice:** [vocabulary, rhythm, tics, what they never say]
  - Sample lines:
    1. "[line]"
    2. "[line]"
    3. "[line]"
- **Look & staging:** [silhouette; where found; what they're doing]
- **Knew the old Danny?** [Yes/No — and how that makes Mark read "off" to them]

## 2. Backstory

[2–4 short paragraphs. Era-true. The stuff players sense but rarely hear in full.]

## 3. Relationship arc (Act 1 → 3)

| Act | Where they stand with Mark | What unlocks |
|---|---|---|
| 1 | [starting band — usually Cold/Flat for Danny's friends] | [intro / first favor] |
| 2 | [warming via favors/quests] | [part quest / muster eligibility] |
| 3 | [payoff] | [climactic help] |

## 4. Book entry (what the player tracks)

- **Wants (favor loop):** [the collectible — e.g., "Bazooka Joe comics", "bottle caps"]
- **Leads (threads):** [one-line, with thread doodle 🔧/👥/✉️]
- **Note reading notes:** [how they ring — and any special case, e.g., Iwona rings "strange"]

## 5. Dialog Map

### 5.1 Greeting matrix (bark layer)

| | Cold/Flat | Warming | Warm | Close |
|---|---|---|---|---|
| **Act 1** | "[line]" | "[line]" | "[line]" | — |
| **Act 2** | "[line]" | "[line]" | "[line]" | "[line]" |
| **Act 3** | — | "[line]" | "[line]" | "[line]" |

### 5.2 Node table (story / topic / quest layers)

| Node ID | Layer | Conditions (`act`/`rel`/`quest`/`flags`) | Line(s) | Choices → target | Effects |
|---|---|---|---|---|---|
| `name_meet` | Story | act≥1 ∧ ¬`met_name` | "[first-meeting line]" | — | set `met_name` |
| `name_topic_x` | Topic | `met_name` | "[ask-about line]" | → … | — |
| `name_qXX_active` | Quest | `quest[Q-XX]`=Active | "[branching exchange]" | A→… / B→… | give [part]; rel +1 |

## 6. Cross-refs

- Quests: [Q-XXX …]
- Systems: `../components/relationship-instrument.md`, `../design-spine.md`
- Source: `../intake/people.yaml` → [entry]
