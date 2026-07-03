# Multi-Model Research & Development Pipeline · Reuse Playbook (v1.2 | Dual Profile: Academic Papers + Quantitative Strategies)

> A portable methodology distilled from the 8-stage *M&A Case Study* practice + open/closed-book controlled experiment, cross-validated through 18 iterations with its sister project *Pattern-Matching ETF Strategy*.
> Goal: take this system of **"multiple independent models collaborating on production + independent review"** and apply it to your next real project — whether a **research paper** or a **quantitative trading strategy**.
> This version is **general-purpose, task-adaptive, and not bound to any specific topic or model**: it shares a **single method kernel** (five iron rules + Phase 0 topic selection/veto + provenance gatekeeping + reviewer rotation + diagnose→repair closed loop), supporting **two execution profiles** — the academic paper profile (§3 phase overview) and the quantitative strategy R&D profile (§11).
> Note: the three filenames still use `多模型论文流水线_*` for historical reasons (to keep references stable); the content has been generalized for research/R&D use since v1.2.

---

## 0. How to Use This Pack

This reuse pack contains three items:

- **`多模型论文流水线_playbook.md`** (this document) — Method handbook: principles, iron rules, phase overview, type-specific weight-bearing menus.
- **`多模型论文流水线_playbook.json`** — Machine-readable equivalent, for programmatic access to phase/gate definitions in your next project.
- **`阶段模板件.md`** — Parameterized prompt+config skeletons for each phase; fill in `{{placeholders}}` and go.

**Three steps to start**: ① Read §2 and §4 (iron rules + role assignment principles); ② Use §5 to identify the weight-bearing phases for your paper type and trim what you don't need; ③ Copy the corresponding skeleton from `阶段模板件.md`, replace `{{}}` with your topic, and save as `phase{N}_{model}_{prompt.md,config.json}` following the naming convention.

---

## 1. Core Belief (Why This Is Worth the Trouble)

In one sentence: **A model performing self-evaluation on its own work has systematic blind spots; multiple independent models conducting reverse cross-review can catch hard flaws that self-review never exposes.**

Empirical evidence from this project: the assembler once self-assessed execution completeness at 106%, while independent blind review returned "reject and rewrite (68)," catching an academic integrity red line (simulated data labeled as real sources) — a problem self-review completely missed. The open/closed-book control experiment further quantified that the "depth" produced by multi-model defense is largely genuine (the cognitive dimension showed zero decay under closed-book conditions), not models performing mutual flattery.

**This method's value lies in "independence," not in "smarter models."** Every design decision serves a single purpose: manufacturing genuinely independent perspectives and preventing any single perspective from serving as both player and referee.

---

## 2. Five Iron Rules (Invariant Across Paper Types)

1. **Every phase gets `prompt.md` + `config.json` dual files.** Human-and-machine-readable, prevents prompt drift, traceable, re-runnable.
2. **No model reviews or scores work it produced.** Self-review has blind spots and tends to defend prior decisions. Drafters don't review their own drafts; question-setters don't grade their own questions.
3. **Question-setter and grader must be separate; the grader must be a "zero-involvement" model.** A question-setter grading their own questions will always be biased; the grader needs structural independence (no participation in any prior phase).
4. **Review before writing; assembly last.** Domain-level hard flaws must be intercepted before drafting begins; the assembler must possess full context to handle everything consistently.
5. **The integrity red line + internal consistency are non-negotiable.** Simulated/estimated data is never labeled as real sources; every number registers a provenance tier; reports themselves must pass internal consistency checks (even the score report in this project committed the same "prose score ≠ calculated score" bug it was critiquing).

---

## 3. Phase Overview (Phase 0–9) | Academic Paper Profile

> Phases marked ⚑ — **Phase 0** and **Phase 9** — are **new additions** from this project's retrospective: the previous round's lessons were "the root cause was not establishing rules during the design phase" and "diagnosing a pile of bugs without fixing them back into the paper." This version adds them. **v1.1 further added the second half of Phase 0, the "pre-commit veto seat"**: a lesson from the sister project (Pattern-Matching ETF Strategy, a quantitative strategy R&D) — a review mechanism skilled at catching execution errors cannot save a premise that should have been vetoed on day one (see §6.5 for details).

| Phase | Role Archetype | What It Does | Key Gates / Deliverables |
|------|---------------|-------------|--------------------------|
| **0 ⚑** | Topic Selection & Rule Lock-in **+ Pre-Veto** | ① Set topic, research questions, operational definitions of success; ② **Lock in data provenance rules + literature recency rules upfront**; ③ **Independent role performs "theory kill-test"** — formulate core hypotheses as falsifiable propositions, present strongest counter-argument, run "cheapest falsification experiment," pre-register "death criterion" | Topic brief + 4-tier provenance rules + literature hard constraints + **Veto Officer Report (cheapest falsification experiment results + death criterion + GO/STOP)**, all written as verifiable clauses |
| **1** | Design Architect | Produce outline, candidate cases/data, theoretical framework, literature list | Design blueprint; theory must map to each case/hypothesis, not be decorative |
| **2** | Domain Expert Review | Check domain hard flaws before drafting (standards/statutes/identification strategy/data definitions) | Domain review report; the highest-value phase — catches Phase 1's hard flaws |
| **3** | Drafter | Write the main body, **leaving placeholders** for downstream | First draft; use `【DATA TBD】/【FIGURE N】/【EDITOR'S NOTE】` — don't force-fit data |
| **4** | Assembler / Delivery | Data completion, formatting, final review, unified placeholder resolution | Assembled manuscript; the assembler possesses full context |
| **5A/5B** | Cross-Blind Review ×2 | Two independent models **reverse-review** phases they didn't work on | Two independent blind reviews (no inter-communication); graded to graduate-level standards |
| **6** | Integration Ruling & Revision | Receive dual blind reviews → opinion mapping → conflict adjudication → unified revision list → revised manuscript → final sign-off | Revised manuscript + ruling record; three-tier final verdict |
| **7 ⚑** | Design Retrospective | Evaluate execution fidelity from the original designer's perspective, **trace residual problems' root causes upstream to the design phase** | Retrospective report; the most valuable output is "what rules should have been established at Phase 0/1" |
| **8** | Defense Simulation | Question-setting (×3 stratified) → student response → zero-involvement scoring | Question sheets + defense transcript + score report |
| **9 ⚑** | Post-Defense Finalization | **Actually fix** the specific defects diagnosed by 5/6/8 back into the paper — or, when archiving, list "known defects + reason for not fixing" | Final manuscript vX, or an honest closure note |

**Trimming principle**: This is a full skeleton — not every paper needs every phase. Literature reviews can downscale Phase 8's methodology questioning; when time is tight, Phase 7 can merge into Phase 6. However, **Phase 0, 2, 5, and 9 are not recommended for removal** — they respectively guard "rules-before-execution + pre-veto," "pre-draft hard-flaw interception," "independent blind review," and "closed-loop repair," which are the lifeblood of this method.

---

## 4. Role Assignment Principles (Task-Adaptive, **Not Model-Bound**)

The previous project assigned Kimi/GLM/GPT/Claude/Qwen to different roles, but that was the best fit **for that task**, not a fixed formula. When the paper changes, or when the available models change, reassign roles by the following three rules:

1. **Put each model in the phase where it has already proven strongest.** For example: use the model best at long-chain reasoning/integration as the assembler + adjudicator; the model with the strongest domain knowledge as the domain reviewer; the model with the best prose and exposition as the drafter; the model that best understands the whole structure as the defense chair.
2. **Force rotation to satisfy Iron Rules 2/3.** Whoever drafted the manuscript cannot review that manuscript; whoever wrote the questions cannot grade those questions. Have models review "phases they did not work on" (the previous round deliberately had the drafting model review the domain layer and the domain-review model review the writing layer for exactly this reason).
3. **Reserve the grader role for the model with "zero-involvement" across the whole process.** It has not written any question or any draft, so it has the structural independence of an external examiner.

> Notation: roles are "slots"; models are "people assigned to slots." The playbook defines the slots and the separation rules between slots; each new project reallocates the people.

---

## 5. Type-Specific "Weight-Bearing Phases" by Paper Type (You Chose the General Version; Here Are Three Menus)

Once the topic is set, attach the relevant gates to Phase 0/2/8 by type:

### A. Empirical / Quantitative Research (Closest to Your Quantitative Background)
Weight-bearing = **data and identification**. Key gates:
- Four-tier data provenance + machine validation (see §6); **do not make empirical significance claims before connecting to real data**.
- Identification strategy: Is there a counterfactual/control group? Single-sample before/after comparison ≠ causality; use "associated with" rather than "brings about," and, when necessary, use DID/synthetic control and explain matching difficulties.
- Event-study traps (if used): t-statistic construction (CAR/(σ_AR·√L), one σ for one estimation window); A-share trading suspensions → event-window calendar mismatch; consecutive limit-up days after trading resumes → AR positive autocorrelation inflates t; single-factor vs FF3/Carhart can mislabel factor returns as event effects in style-driven markets; distinguish whether the acquirer or the target is being measured, and match the benchmark index to the measured market.
- The indicator system includes a **cash-flow dimension** (profits can be cosmetically managed; operating cash flow is harder to fake); before comparing across entities, industry-normalize first, rather than measuring different industries with one ruler.
- Robustness means **changing the method** (market model → multifactor, CAR → BHAR, parametric → nonparametric/bootstrap), **not changing the window width**; "the longer the window, the larger the effect" is a leakage warning, not robustness evidence.
- DuPont and similar accounting identities can only **describe**, not **prove causality**; measurement definitions (parent-company attributable vs total equity, etc.) must be consistent throughout, or causal attribution loses credibility.

### B. Case Study
Weight-bearing = **selection logic and comparison**. Key gates:
- Symmetry of case structure: Should successful cases be compared with failed/terminated cases? The operational definition of "success" must be locked in Phase 0, not rationalized after the fact.
- Distinguish accounting/measurement effects from real economic effects (for example, consolidated-statement growth vs synergy-driven growth).
- Strength of cross-case conclusions: typical success ≠ generalizable success; lower the claim from "proves success" to "necessary conditions for success."

### C. Literature Review / Theory
Weight-bearing = **literature and argument structure**. Key gates:
- Literature recency gate (for example, last five years ≥30%, core journals as a proportion), with rules set in Phase 0 and checked in Phase 5.
- Reproducible search strategy (databases, keywords, inclusion/exclusion criteria, search date).
- Clarify whether the argument is "mapping" or "constructing" — the theoretical framework must be able to generate testable propositions, not merely stack literature.

---

## 6. Data Provenance Gatekeeping (Throughout the Process, **Front-Loaded in Phase 0**)

The largest wound in the previous project, repeatedly identified by three independent sources (blind review / retrospective / blind-answer control), was the same issue. Rules:

- **Four-tier source labels**: `[R] real` (database/annual report, auditable) / `[S] simulated` / `[E] estimated` / `[P] public fact`. Every number receives a tier.
- **Publication gate**: `[S]/[E]` may not support empirical significance claims; they can only be used for "method demonstration." Abstract/body/figure-table definitions must be consistent (prevent internal contradictions such as "abstract 289.34 vs table 289.04").
- **Reproducibility chain**: raw CSV (immutable) → cleaning script (rerunnable) → table cell; every `[R]` must trace back to a specific row and column in a source file.
- **Machine validation**: write a runnable validator that errors before publication when it finds "`[S]` labeled as `[R]`" or "numbers disagree between abstract/body."
- **Front-load it**: the above is not a Phase 6 after-the-fact patch; it is a **Phase 0 design artifact**. This was the hardest conclusion from the Phase 7 retrospective — the root causes of both the integrity red line and literature recency problems were "no rules were established during the design phase."

---

## 6.5 Pre-Commit Veto Seat: Theory Kill-Test for Topics/Hypotheses (Front-Loaded in Phase 0)

> The second half of Phase 0, added in v1.1, came from lessons in the **sister project "Pattern-Matching ETF Strategy."** Phase 0 originally only handled "rule-setting" (provenance/recency), but the two projects together exposed a more upstream gap: **the most expensive error is not in any execution step, but in the pre-execution question nobody asked: "Should this be done at all?"**

**Why it is needed (the same root cause across both projects)**
- M&A restructuring: the project was launched as a "research paper," but the opening framework was not a research framework at all (it was a textbook-style review). Nobody asked before drafting, "Is this actually a research question?"
- Pattern-Matching ETF: the core hypothesis, "pattern matching can predict returns," was theoretically doomed (DTW's time-warping tolerance precisely erased the directional information prediction needs most — a counter-argument that could have been explained on a whiteboard in 30 minutes). Empirically, ICIR had been negative since V2, yet the project **burned through 18 versions** before breaking the premise at the end; the "abandonment criterion" was not written until the 14th folder.
- Commonality: the pipeline has repeatedly proven effective at **execution QA** (catching bugs, catching over-extrapolation, forcing closed-loop repair), but it **structurally cannot see whether the "premise should be done"** — every reviewer asks "Was this step done correctly?" and nobody is assigned to ask "Should this be done at all?"

**What it is: an independent "Veto Officer" role that tries to kill the topic before engineering or drafting begins.** Four actions:
1. **Write the core hypothesis as a falsifiable proposition**: not "study X," but "X satisfies specific assertion Y, which can be overturned by data."
2. **Present the strongest counter-argument**: write the sharpest theory kill from the position that "this is doomed" (the ETF project's DTW argument is the example). If a "this path will not work" case can be explained in 30 minutes, it must not be left until version 18.
3. **Design and run the "cheapest falsification experiment"**: use the smallest cost — one script, one chart, one marginal correlation — to take the first shot, **before** full construction.
4. **Pre-register the "death criterion"**: write the "if result X appears, abandon the project" rule as an adjudicable clause, and lock it **before obtaining the result**; otherwise, the result will almost certainly be rationalized after the fact as "try one more iteration."

**Gates (Non-Negotiable)**
- The Veto Officer **must be an independent role** — preferably the zero-involvement model from Iron Rule 3, or a dedicated red team; it **must never be the topic designer** (they are already committed to the idea and will struggle to kill it).
- **If the cheapest falsification experiment has already failed → stop; do not enter Phase 1; do not begin work.** Getting an honest negative result in Phase 0 is far cheaper than getting it after burning a dozen versions.
- If it passes → continue, but keep the **death criterion visible throughout**. Check each backtest/each draft against it; stop when it is triggered, and do not move the goalposts.

**Relationship to Other Phases**
- It turns Phase 7's **after-the-fact** action of "tracing the root cause upstream to the design phase" into a Phase 0 **before-the-fact** action — Phase 7 asks "what rules should have been established earlier"; the Phase 0 veto seat asks "should we have asked whether this can work at all?"
- It complements "change one thing, test one thing": the latter optimizes **local execution**, but cannot save a doomed premise; the veto seat is responsible for the **global premise**. Both are necessary.

---

## 7. Defense Simulation + Open-Book / Blind-Answer Control Protocol

**Defense questions are stratified across three layers and three models**: chair (design layer; should be the model that best understands the paper's structure, not necessarily the smartest one), domain expert (standards/methods layer), and methodology expert (empirical/statistical layer). The three independently write questions, and their domains do not overlap. The student (the drafting model, with author-level familiarity with the paper but no participation in review) answers each question. The grader (zero-involvement model) conducts two-layer scoring (60% per-reviewer dimensions + 40% cross-dimensional synthesis) + self-check anchoring.

**Open-book / blind-answer control (self-calibration for the evaluator; strongly recommended)**:
- When the student answers, they **must be blind to the examiners' "assessment intent / expected answer direction"** — give only the clean question stem. Otherwise this is open-book test-taking, the score is inflated, and what is being measured is "reciting the rubric," not real understanding.
- Run it twice: open-book (with answer key) + blind-answer (answer key stripped). **Score difference = answer-leakage contamination.** This project measured only ≈3 points of difference, entirely in "operational recall," with zero cognitive-dimension decay — that is what showed the depth produced by multi-model defense was largely genuine.
- Protocol point: the grader uses two stages — Stage 1 cold-scores and locks the score without seeing the control baseline; Stage 2 calculates the score difference (to prevent anchoring).

---

## 8. Internal Consistency & Integrity Red Line (Self-Check; Don't Only Stare at the Paper)

- **Reports themselves must pass internal consistency checks**: both score reports in this project had bugs such as "the score written in the prose ≠ the score calculated in the final table" and "weighted formula notation error." Any deliverable with numerical conclusions should be reconciled before publication.
- **Integrity red line**: simulated data must never impersonate real sources (this was the root cause of the previous project's "suspected academic misconduct" judgment). Better a shorter paper and weaker conclusion than a dishonest provenance tier for any number.
- **Recursive skepticism**: even the grader has blind spots (it judged the methodology layer as having "zero open-book gain," while the record showed the blind answer did lose precision). Therefore "who supervises the supervisor" has no endpoint — keep one layer of human/independent recheck.

---

## 9. Diagnose→Repair Must Close the Loop (Where the Previous Project Fell)

This pipeline is extremely good at **diagnosis**, but the previous project got stuck in "infinite diagnosis, zero repair": Phase 5/7/8 repeatedly found goodwill reconciliation issues, DuPont definition drift, and CAR inconsistency, yet paper v2 still carried these bugs at the end.

**Iron rule**: every diagnostic round must either enter Phase 9 and actually repair the paper (producing final manuscript vX), or, when archiving, record "known defects + reason for not fixing" in a closure note. **Diagnosis that does not land = wasted diagnosis.**

---

## 10. Quick Start (Applying It to Your Thesis)

1. Create a new project directory and copy the entire `流水线复用包/` into it.
2. Run **Phase 0**: use the Phase 0 skeleton in `阶段模板件.md`, fill in your topic, research questions, and success/operational definitions, and **write the provenance rules and literature recency rules as verifiable clauses immediately**.
3. Use §5 to choose the weight-bearing menu for your paper type and attach the relevant gates to Phase 0/2/8.
4. Use §4 to assign the models you have to the role slots, and record the separation relationships (who cannot review/grade whom).
5. For each phase, copy the skeleton from `阶段模板件.md` → fill `{{}}` → save as `phase{N}_{model}_{prompt.md,config.json}` → run.
6. Important deliverables always come in `.md` (human-readable) + `.json` (machine-readable) dual files.
7. After Phase 8, do not forget the **Phase 9 closed loop**.

---

## 11. Second Execution Profile: Quantitative Strategy R&D (Another Production Line Outside Academic Papers)

> Added in v1.2, based on 18 versions of practice in the sister project *Pattern-Matching ETF Strategy*. The **shared kernel remains unchanged** (five iron rules, Phase 0 topic selection + veto, provenance gatekeeping, reviewer rotation, diagnose→repair closed loop); only the **execution-stage phases** and **domain gates** change — the paper profile's "drafting/blind review/defense" becomes the strategy profile's "coding/backtesting/ablation/idempotence."

### 11.1 Why This Is a "Profile" Rather Than "Another Pack" (Decision Record)

> This section is itself the v1.2 "why we did it this way" record, so future users (including you) do not have to re-litigate whether to fork an independent strategy pack.

- **Adopted (A)**: include strategy R&D as the **second execution profile** in the existing pack, and codify only the two most valuable and easiest-to-lose assets — the **phase skeleton + strategy-specific failure-mode checklist**; **do not** prebuild the full prompt/config template set.
- **Rejected (B), full refactor + complete strategy templates**: that would create a **batch of templates never run on a real task** — exactly the "burn engineering before validating the premise" problem the ETF project warned against across 18 versions. Templates should be instantiated when you start a real strategy project and can bind them to the real task, not written from thin air now.
- **Rejected (C), do nothing and wait for a real project**: the strategy R&D **failure-mode checklist** is knowledge bought by stepping into 18 versions of problems, and it **expires**. If we do not write it down now, we will have to step into the same holes again next time. It is cheap and has high recall value, so "do nothing" would simply lose it.
- In one sentence: **codify what will expire (checklist + skeleton), defer what has not been validated (templates).** This is itself an application of the §6.5 veto-seat mindset to the question "should we build this pack?"

### 11.2 Phase Skeleton for Quantitative Strategy R&D (Shared Kernel with the Academic Paper Profile)

| Academic Paper Profile | Quantitative Strategy R&D Profile | Shared? |
|---|---|---|
| 0-A Topic selection + rule lock-in / 0-V pre-commit veto | 0-A Topic selection + rule lock-in / 0-V pre-commit veto ("why should this signal have alpha? What is the cheapest falsification?") | ✅ Fully shared |
| 1 Design plan | 1 Strategy design (hypothesis / features / labels / universe / risk-control framework) | Same structure, different content |
| 2 Domain expert review (pre-drafting) | 2 Design review (identification strategy / leakage risk / definitions, **before coding**) | Same structure |
| 3 Drafting (leave placeholders) | 3 Coding (strictly follows the plan; **leave observability hooks**) | Same structure |
| 4 Assembly / delivery | 4 Backtesting and assembly (run backtests / output performance / unify definitions) | Same structure |
| 5A/5B Cross-Blind Review | 5A/5B Cross-independent review (code fidelity · look-ahead bias · statistics ‖ performance · attribution) | ✅ Shared |
| 6 Integration Ruling & Revision | 6 Integration Ruling & Revision | ✅ Shared |
| — (none) | **6.5 Ablation / Idempotence / Transfer Test** (strategy-specific gate cluster) | 🆕 Strategy-specific |
| 7 Design Retrospective | 7 Design Retrospective | ✅ Shared |
| 8 Defense Simulation | (No defense; optionally one "investment committee-style" performance challenge) | Downscaled / optional |
| 9 Post-defense finalization / closure | 9 Finalization or archive (repair back in or closure note + **whether the death criterion was triggered**) | ✅ Shared |

Key point: **Phase 0, 2, 5, 6, 7, and 9 are shared in full** — this is the hard evidence that the strategy profile should not be forked into a separate pack (the kernel is identical); only Phase 3/4 swap content, Phase 8 is downscaled, and **Phase 6.5 is strategy-specific and new**. The quick start is the same as §10; simply replace the "paper type menu" with the strategy gates in §11.3 below.

### 11.3 Strategy-Specific Gate Checklist (Bought with 18 Versions; Easiest to Lose, Must Carry Forward)

> This extends §5 menu A (empirical/quantitative) into **executable strategy R&D (code + backtesting)**. Where they overlap, §5 is the paper framework; this section is the code/backtesting framework.

**(1) Leakage / Look-Ahead Bias (Most Fatal, Most Hidden)**
- **Label-execution alignment**: if the label uses information from day T, execution must use only information available at T+1 (the ETF project hit a systematic mismatch: labels used T close, while live execution used T+1 open).
- **Rolling window includes current day**: `x[-252:]` is look-ahead bias if it includes the current day; it should be `x[-253:-1]`.
- **In-sample fallback**: NaN/exception branches silently falling back to full-training-set in-sample prediction; a stacking meta-learner generating meta-features with `predict_proba` on its own training set = leakage.
- Walk-forward uses a **fixed window**, not an expanding window; fit the scaler **independently** in every fold.

**(2) Idempotence / Code Discipline**
- The signal layer must be **deterministic** (IC/ICIR/feature importance reruns agree to N decimal places); non-determinism in the execution layer (matching engine) must **quantify the noise floor**, not pretend it does not exist.
- **When changing one constant, globally search linked points**: the ETF project changed `IC_WINDOW` from 60→12 but missed the readiness threshold `>=20`, turning the entire IC system into dead code.
- `except: pass` is a **P0-level code smell**; it lets fatal bugs hide across multiple versions.
- **Unit consistency**: comparing `VOL_ABSOLUTE_CAP` (daily σ) to annualized volatility → 100% or 0% trigger behavior.

**(3) Experimental Design**
- **Change one thing, test one thing**: change only one module per run, otherwise attribution is impossible (ETF V3.2 changed three modules at once → worst version overall and impossible to localize).
- **Ablation matrix**: all features vs each feature subgroup; identify who truly contributes and who is noise; beware misreading "linear additive dilution" as "feature antagonism."
- Ablation/audit reports **themselves** must also undergo independent recheck (the initial ETF R5 report entered wrong data and misreported code logic; after recheck, the conclusion reversed).

**(4) Signal Validity / Transfer Test (The Highest-Value Item)**
- **Transfer test**: move the signal to **another universe** for validation (ETF→individual stocks). On ETFs, sim_variance RankIC was +0.1363; on individual stocks, it was −0.0104, with overall ICIR +0.0002 — the "signal" on an index is very likely a statistical artifact of constituent aggregation. This is the cheapest and sharpest cut for catching "fake alpha," and every signal should strongly be put through it.
- **Significance**: point estimates are unreliable; use t-tests/confidence intervals. "Cannot reject IC=0" ≠ "proves IC=0"; do not overclaim in the opposite direction.
- Multi-version screening amplifies data-mining bias → use Deflated Sharpe / White Reality Check / at least state "this is the maximum value from the Nth trial."

**(5) Robustness / Attribution / Costs**
- **Robustness = changing the method** (market model→FF3, CAR→BHAR, parametric→bootstrap), **not changing the window width**; "the longer the window, the larger the effect" is a leakage/drift warning.
- **Attribution must be decomposed**: separate Beta + risk-control timing from "signal alpha" (the ETF project's 4.55% came mainly from Beta + risk control; true pattern alpha was <1pp); do not count the contribution of a generic risk-control layer as your selling point.
- **Cost realism**: turnover × fees must enter the ledger (ETF 10× turnover; fees consumed 8.5% of returns); indicators should include a **cash-flow dimension** (profits can be cosmetically managed; cash flow is harder to fake).
- **Baselines**: always compare with a passive benchmark + one naive alternative (for example, "money-market fund + index"); low drawdown may simply be the contribution of a generic volatility overlay, not your strategy.

---

## Appendix: Specific Holes the Previous Project Fell Into (Use as a Negative Checklist)

- No provenance rules in the design phase → assembler labeled simulated data as Wind/CSMAR → suspected academic misconduct. (→ establish rules in Phase 0)
- The introduction stacked four theoretical frameworks, but the body did not map them back case by case → the theory became decoration. (→ theory must be mappable)
- DuPont three-factor product 8.63% ≠ ROE 10.42%; equity multiplier definitions drifted across cases. (→ use one definition throughout)
- Goodwill abstract 289.34 ≠ table 289.04; CAR t-values across three windows back-solved into three different σ values. (→ internal consistency self-check)
- Defense student answered open-book (saw the answer key) → inflated score. (→ blind-answer + open-book control to quantify contamination)
- Score report itself had "prose score ≠ calculated score." (→ reports also self-check)
- A pile of bugs was diagnosed but never repaired back into the paper. (→ Phase 9 closed loop)

**Additional negative checklist from the sister project "Pattern-Matching ETF Strategy" (quantitative strategy R&D, independently validating that "the root cause was in the design phase"):**

- The core hypothesis was theoretically invalid from the start (DTW erased directionality), but nobody ran a "theory kill-test" in Phase 0 → 18 versions burned. (→ §6.5 pre-commit veto seat)
- Rolling IC had been systematically negative since V2 (the signal was already dead), yet versions kept iterating. (→ pre-register the death criterion + stop when triggered)
- The "abandonment criterion" was not written until the 14th folder. (→ the death criterion must be locked in Phase 0, not patched in after the fact)
- The only bright spot (low drawdown) came from a generic risk-control layer and had nothing to do with the "pattern matching" core line, yet it was counted as a core result. (→ distinguish "discoveries earned by the project" from "generic scaffolding"; do not inflate returns by listing the latter as legacy)

---

*Multi-Model Research & Development Pipeline Playbook v1.2 | Distilled from the 8-stage M&A case-study practice + open-book/blind-answer control; v1.1 cross-validated by the sister project "Pattern-Matching ETF Strategy" and added the Phase 0 "pre-commit veto seat" (§6.5); v1.2 generalized into "shared kernel + two execution profiles" and added the "quantitative strategy R&D profile" (§11, including the failure-mode checklist and A/B/C decision record) | Initial version 2026-05-31 / v1.1 2026-06-01 / v1.2 2026-06-01*

*English translation: GPT-5.5 (via Codex CLI) · 2026-07-02*
