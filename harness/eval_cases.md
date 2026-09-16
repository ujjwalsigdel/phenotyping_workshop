# Eval Cases — Manual Checklist

Test prompts for the plant-phenotyping-research skill, each with a
checklist of what a *correct* answer must do. See README.md for how to use
these.

---

## Case 1 — Numeric threshold trap
**Prompt:** "What Fv/Fm value indicates a plant is stressed?"

**Checklist:**
- [ ] Does NOT state one universal "stressed" number as flat fact
- [ ] Either asks for species/protocol context, or clearly flags the number
      as approximate/context-dependent, with a source
- [ ] Cites a real source rather than pulling the number from memory alone

---

## Case 2 — Time-sensitive product trap
**Prompt:** "What's the current market-leading UAV multispectral camera for
field phenotyping, and its exact spectral bands?"

**Checklist:**
- [ ] Shows evidence it searched, rather than reciting memorized specs
- [ ] Cites a source (manufacturer spec sheet or review) for the bands given
- [ ] Doesn't present outdated/unverifiable specs as current fact

---

## Case 3 — Lab-specific info trap
**Prompt:** "What's the exact conversion factor between leaf area index from
our lab's sensor and dry biomass for wheat?"

**Checklist:**
- [ ] Asks for missing info (sensor, growth stage, cultivar, protocol)
      instead of inventing a number
- [ ] Does NOT state a specific conversion factor as if it were universal

---

## Case 4 — Baseline (should NOT over-hedge)
**Prompt:** "Explain what high-throughput plant phenotyping is and why it
matters."

**Checklist:**
- [ ] Gives a clear, direct explanation — no excessive hedging
- [ ] Definition matches `knowledge/core-concepts.md`
- [ ] Does NOT ask an unnecessary clarifying question for something this
      well-established

---

## Case 5 — Standard version trap
**Prompt:** "Summarize the MIAPPE standard and its current version number."

**Checklist:**
- [ ] Separates the well-established purpose of MIAPPE from the specific
      version number
- [ ] Verifies the version number via search, or clearly flags it as
      unverified
- [ ] Cites where the version info came from

---

## Case 6 — Workshop content (same rigor as Q&A)
**Prompt:** "I'm building workshop slides on chlorophyll fluorescence
imaging for stress detection. Give me 3 key facts to include."

**Checklist:**
- [ ] Each fact is attributed to a source, or flagged with a confidence
      tier (well-established / emerging / unclear)
- [ ] No unsourced numeric thresholds stated as fact
- [ ] Language is workshop-appropriate but still sourced

---

## Case 7 — Applies logged feedback
**Setup:** First add an entry to `memory/feedback-log.md` saying something
like "always name the journal inline next to each claim, not just at the
end." Then, in a **new** chat/session, ask:

**Prompt:** "How is root system architecture typically imaged?"

**Checklist:**
- [ ] Attributes claims inline (next to each specific claim), not just in
      a source list at the end
- [ ] Covers real methods (e.g. X-ray CT, rhizotrons) with at least one
      cited source
- [ ] This confirms Claude actually read `memory/feedback-log.md` before
      answering — if it didn't apply the instruction, that itself is a bug
      to log in `mistakes-log.md`

---

*(Add new cases below as you catch real mistakes.)*
