---
stepsCompleted: ["step-01-validate-prerequisites"]
inputDocuments: 
  - '_bmad-output/planning-artifacts/prds/prd-project-map-bmad-2026-09-01/prd.md'
  - '_bmad-output/planning-artifacts/architecture/architecture-project-map-bmad-2026-09-02/ARCHITECTURE-SPINE.md'
  - '_bmad-output/specs/spec-battle-map-stage-2-final/SPEC.md'
---

# Battle Map — Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for Battle Map, decomposing the requirements from the PRD, Architecture Spine, and SPEC into implementable stories.

## Requirements Inventory

### Functional Requirements

**FR1: Project Goal Definition & Tracking**  
系统必须支持定义项目的终极目标，以可验证的行为/条件形式表达成功标准，让用户理解项目最终达成什么现实结果。

**FR2: Complete Functions Structure**  
系统必须以能力完整的形式展示功能结构：每个独立能力有输入要求、核心行为契约、输出保证、对整体目标的贡献说明，而不是执行单元粒度。

**FR3: Regions Grouping**  
系统必须支持将相关功能聚类成区域共享关注点或依赖关系，但不强制严格层级。

**FR4: Milestones Capability Evidence**  
系统必须定义可针对实际系统行为验证的里程碑，描述系统现在具备的真实能力变化。

**FR5: Structure Relations Network**  
系统必须展示四种基本关系类型：串行（serial）、并行（parallel）、依赖（dependency）、汇合（join），并支持在实现过程中动态修改。

**FR6: Frontier Execution State View**  
系统必须实时展示当前执行前沿状态：active/ready/blocked/completed 四类工作，以及基于结构和边界的下一步可选行动。

**FR7: Boundary Management**  
系统必须维护三类一等边界：current-validity boundary（已被接受足以推进）、unknown boundaries（结构性不确定未测试）、invalidated boundaries（先前接受的假设不再适用）。

**FR8: Candidate Structural Proposals**  
系统必须允许提出对地图形状的结构变更提案（来自新暴露的依赖、改变的未知边界、方法教训），并与已采纳形状保持清晰区分。

**FR9: Causal Narrative Network Recording**  
系统必须支持记录 requirement/commitment/problem/contradiction/explanation/correction/supersession/lesson/impact 等一等语义对象及其时间/因果关系的追加写入叙事；不同关系类型允许不同结构投影，不强制每条统一 schema。

**FR10: Next Move Recommendation with Rationale**  
系统必须为每次下一步推荐提供可解释的理由：基于当前前沿状态、结构风险降低潜力、未知边界减少价值、所有者策略一致性。

**FR11: Advancement-Driven Action Class Selection**  
系统必须读取当前 Project Shape / unknowns / frontier / owner policy，自动选择或推荐下一行动类并编译 frozen bootstrap；只有当 authority policy 要求时才由用户/责任方批准、覆盖或纠偏；用户交互接口通过选择动作类别（explore/shape/implement/verify/close）来触发自主 worker，无需了解外部术语或角色标题。

**FR12: On-Demand Source Context Access**  
系统必须在需要时支持按需回到外部原生来源获取当前判断所需的事实上下文，但这些是临时访问入口，不是持久化存储。

### Non-Functional Requirements

**NFR1: Battle Map Native Vocabulary Understandability**  
所有 Battle Map 词汇必须完全可理解，无需任何 BMAD 先验知识作为前提条件。

### Additional Requirements (Architecture Constraints)

AR1-AR15: Seven-Layer Architecture, ADOPTED/CANDIDATE model, Region Maturity States, Weaving Protocol, Advancement Coordinator, Deterministic Control Plane, Semantic Mutation Port, Composable Role Identity, Query Interfaces, Verification at Joins, Brownfield Compatibility, Technology Neutrality, Qualitative Metrics, Not-a-Forensic-Archive, Derived Views constraints as specified in Step 1 extraction.

### FR Coverage Map

FR1 → Epic 1 (Core Shape Definition)  
FR2 → Epic 2 (Functions & Regions)  
FR3 → Epic 2 (Functions & Regions)  
FR4 → Epic 3 (Milestones & Validation)  
FR5 → Epic 4 (Structure Relations)  
FR6 → Epic 5 (Frontier & Advancement)  
FR7 → Epic 6 (Boundary Management)  
FR8 → Epic 7 (Candidate Proposals)  
FR9 → Epic 8 (Narrative System)  
FR10 → Epic 5 (Frontier & Advancement)  
FR11 → Epic 5 (Frontier & Advancement)  
FR12 → Epic 9 (Source Context Access)  

NFR1 + AR1-AR15 → All epics (cross-cutting constraints)

## Epic List

### Epic 1: Core Project Shape Definition — Goals, Functions, and Regions Foundation

**User Outcome:** Users can define and manage the complete project structure with goals, functions, and regions that express capability-complete units rather than task lists. They understand what the project becomes and how capabilities combine to achieve the ultimate result.

**FRs covered:** FR1, FR2, FR3  
**User value:** First screen answers "what does this project become" without needing BMAD terminology.

### Epic 2: Milestone-Based Capability Validation — Verifiable Behavioral Evidence

**User Outcome:** Users can define milestones as observable behavioral changes that verify system capability progression, not document states or execution status. Each milestone communicates what real capability the system now possesses.

**FRs covered:** FR4  
**User value:** Clear evidence that the system has achieved intended capabilities through verifiable behaviors.

### Epic 3: Structure Relations Network — Dependencies, Parallelism, Joins, and Dynamic Modification

**User Outcome:** Users see and manage relationships between all structural elements—serial dependencies, parallel paths, cross-dependencies, and natural joins—and can modify these relations as implementation exposes false assumptions.

**FRs covered:** FR5  
**User value:** Understanding of how nodes connect and evolve; avoids premature commitment by allowing dynamic relation updates.

### Epic 4: Frontier Execution State & Recommended Actions — Active Work, Ready Queues, Blocked Paths

**User Outcome:** Users view current execution frontier showing active work, ready-to-start items, blocked paths with reasons, and completed capabilities; receive recommended next moves with explicit rationale tied to structure and unknown boundaries.

**FRs covered:** FR6, FR10, FR11  
**User value:** Knows exactly what to do next and why; sees blocked paths with reasons; understands recommendation logic without arbitrary scheduling.

### Epic 5: Validity, Unknown, and Investment-Boundary Management

**User Outcome:** Users clearly distinguish between accepted-but-unverified boundaries, structurally uncertain areas, and previously-accepted assumptions that are no longer valid; makes investment judgments based on confidence levels.

**FRs covered:** FR7  
**User value:** Explicit understanding of confidence vs. speculation; informed decisions about which parts of structure can guide advancement.

### Epic 6: Candidate Structural Changes with Adopted/Pending Distinction

**User Outcome:** Users can propose structural revisions immediately when reality changes, see them distinguished from adopted shape, track owning authority decisions, and watch rejected candidates leave no permanent record unless they taught lessons.

**FRs covered:** FR8  
**User value:** Immediate preservation of new project understanding while keeping clean distinction between "noticed" and "adopted."

### Epic 7: Causal Narrative Network — Requirement/Commitment/Problem/Lesson Time-Cause Relationships

**User Outcome:** Users query narrative entries to understand why the project became shaped this way, seeing causal links between prior directions, triggering realizations, new judgments, impacts, lessons, and superseding relationships—without replaying raw incident details.

**FRs covered:** FR9  
**User value:** Explains structural change causality, not chronology; reusable lessons worth repeating or avoiding.

### Epic 8: Adaptive Source Context Access — Temporary Fact Retrieval Behind Semantic Core

**User Outcome:** When distilled semantics alone cannot make a judgment, users can access on-demand source context with clear indication of which decision needs it and what should be distilled; raw facts remain external or temporary workset.

**FRs covered:** FR12  
**User value:** Raw facts available when needed but never accumulate as durable project semantics.

### Epic 9: Cross-Epic Architecture Foundations — Seven-Layer Backbone, Semantic Versioning, and Worker Discipline

**User Outcome:** System implements consistent architecture across all epics: seven-layer data/control loop, single semantic-version consistency boundary, deterministic worker control plane, composable role identity, verification-at-joins protocol, brownfield compatibility shims, technology neutrality, qualitative metrics discipline, non-forensic-archive constraint, derived-views-only pattern.

**FRs covered:** NFR1, AR1-AR15 (cross-cutting constraints)  
**User value:** Reliable quality guarantees without requiring knowledge of internal mechanisms; battle-map-native ontology primary throughout.

---

## Dependency Analysis

**Natural Dependencies:**
- Epic 1 → Epic 2: Functions/regions foundation enables milestone definition
- Epic 1 → Epic 3: Capabilities enable relation network construction
- Epic 2+3 → Epic 4: Milestones + relations enable frontier visualization
- Epic 4 → Epic 5: Frontier state requires validity/unknown boundaries
- Epic 1-5 → Epic 6: Shape foundation supports candidate proposals
- Epic 4-5 → Epic 7: Boundaries drive narrative causality
- All epics depend on Epic 9: Architecture foundations apply universally

**Parallel Execution Opportunities:**
- Epic 1 & Epic 2: Can proceed independently (both foundational)
- Epic 4, 5, 6: Can work in parallel once Epics 1-3 complete
- Epic 7: Independent until Epic 6 shapes reach maturity

**Key Join Points:**
- After Epic 1-3: Natural join for verification before building frontier features
- Before Epic 9 deployment: Must observe real deployment patterns before selecting physical carrier

---

## Epic Design Rationale

**Organization principle:** User-value-based grouping (not technical layers). Each epic delivers complete functionality for its domain and enables future epics without creating unresolvable blocking dependencies.

**File-churn consolidation:** Epics touching same core files grouped together where meaningful overlap exists (Epic 1's goal/function/region modifications form one cohesive component; Epic 9's infrastructure touches everything but is self-contained).

**Risk-based splitting:** Fewer large epics chosen because outcome is certain direction confirmed by final PRD/Final SPEC/Final Architecture; early feedback could still change direction on boundary/investment-confidence questions, hence dedicated Epics 5-6 for experimentation.

---

**Confirm [C] to continue to Story creation OR indicate restructuring needs.**