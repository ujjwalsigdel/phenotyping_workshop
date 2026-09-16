# Core Concepts — Seed Knowledge Base

**Status: seed knowledge, not verified against current literature.** Treat
every entry here as a starting orientation, not a citable fact. Before using
any of this in an answer, verify specifics (numbers, thresholds, current
tool names) via search per `references/tier1-sources.md`. When you do verify
something here (or add something new) with a real Tier-1 citation, update the
entry and add a source + date.

---

### What is plant phenotyping?

The measurement of an organism's observable structural and functional traits
(the phenotype), which result from the interaction of its genotype with the
environment. In agricultural/breeding contexts, phenotyping links genetic
variation to measurable traits (yield, stress tolerance, morphology).
*Verify current definitional nuance/consensus before quoting authoritatively.*

### High-throughput phenotyping (HTP)

The use of automated/semi-automated imaging and sensing to measure plant
traits on many plants over time, replacing slow manual measurement — the
response to genomics outpacing the ability to phenotype large populations.
Common settings: controlled-environment conveyor/gantry systems, field
robots/rovers, UAV (drone) platforms, fixed-sensor field stations.
*Verify current platform names/capabilities — this is a fast-moving field.*

### Common imaging modalities

- **RGB imaging** — visible-light images; used for morphology, growth,
  canopy cover, color-based traits.
- **Multispectral imaging** — a handful of discrete spectral bands (often
  including near-infrared); used for vegetation indices (e.g. NDVI-family
  indices) related to greenness/vigor/stress.
- **Hyperspectral imaging** — many contiguous narrow spectral bands; used for
  finer biochemical/physiological inference (pigments, water content,
  disease detection) — verify specific index-to-trait claims per source.
- **Thermal (infrared) imaging** — canopy/leaf temperature, often used as a
  proxy related to stomatal conductance / water status.
- **Chlorophyll fluorescence imaging** — probes photosynthetic efficiency
  (verify specific parameter names, e.g. Fv/Fm, against a real source before
  citing — easy to get wrong).
- **3D imaging (structured light, LiDAR, stereo, laser scanning)** — plant
  architecture, biomass proxies, canopy structure.
- **X-ray CT / MRI** — typically root system architecture, non-destructive
  internal structure.

### Typical HTP data pipeline (general shape — verify specifics per platform)

1. Image/sensor acquisition (often multi-modal, multi-timepoint)
2. Preprocessing (calibration, color correction, registration)
3. Segmentation (isolating plant from background)
4. Trait extraction (deriving quantitative traits from segmented data)
5. Statistical analysis / linking to genotype and environment data

### Standards

- **MIAPPE** (Minimum Information About a Plant Phenotyping Experiment) — a
  metadata standard for describing phenotyping experiments so they're
  comparable/reusable. *Verify current version number before citing it —
  standards get revised.*

---

## Verified additions

*(Empty — this section fills in over time as claims get verified with a
real Tier-1 citation during actual use. Format:)*

```
### <topic> — verified YYYY-MM-DD
<the verified fact, in your own words>
Source: <journal/org name> — <what it showed, described not quoted>
```
