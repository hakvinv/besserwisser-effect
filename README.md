# The Besserwisser Effect

**What is the difference between judging an artifact and producing one?**

This project explores the gap between evaluation and production through a formal model, an illustrative dynamics model, and three empirical predictions. It asks whether repeatedly evaluating other people's work can substitute for the experience of creating work yourself.

[**Read the paper →**](Vosteen_2026_Besserwisser_Effect_final.pdf) &nbsp; · &nbsp; [**Try the interactive self-test →**](https://hakvinv.github.io/besserwisser-effect/besserwisser-quiz.html)

## The argument

The paper distinguishes two operations:

- **Verification:** evaluating a supplied candidate against a criterion.
- **Production:** finding or constructing a candidate that satisfies the criterion.

It proposes that the second problem can be computationally harder than the first, and uses that distinction to frame a broader question about expertise. The paper presents a conditional complexity argument under **P ≠ NP**, an information-theoretic comparison, and a model of how accumulated complexity and integration evolve over time.

These are **claims of the paper under its modeling assumptions**. The complexity argument does not by itself establish a general psychological law about critics, students, or creators. The information comparison also depends on how candidates, prior information, and observations are defined; an artifact's bit length alone does not establish how much new knowledge its creator gained.

## What the model illustrates

| Part of the paper | What it examines | Status |
|---|---|---|
| Complexity | Verification and production as different computational tasks | Conditional theoretical argument; depends on the problem definitions and P ≠ NP |
| Information | Bits obtained from evaluation versus information in a produced artifact | Model-dependent comparison, not a measured learning rate |
| Dynamics | The relationship between accumulated complexity and integration | Illustrative model trajectories, not observed data |
| Predictions | Calibration, long-term competence, and the role of production experience | Empirical hypotheses requiring testing |

The paper's numerical illustration uses a domain of size 2²⁰. Its logarithm is **20 bits**; in the stated model, 100 binary evaluations have an upper bound of 100 bits, not 20. This arithmetic comparison alone does not establish that one production act creates 20 new bits of knowledge.

## Three questions for empirical testing

1. Do people with production experience make better-calibrated judgments than people with similar exposure but no production experience?
2. How does the relationship between accumulated complexity and the ability to integrate it change over time?
3. Does early production experience predict later creative or technical output after accounting for other factors?

The paper proposes study designs for these questions. The repository does not contain empirical data validating the predictions.

## Figures and reproduction

The repository includes two scripts that generate conceptual figures. Run them in a clean working directory with Python, NumPy, SciPy, and Matplotlib:

```sh
git clone https://github.com/hakvinv/besserwisser-effect.git
cd besserwisser-effect
python -m venv .venv
source .venv/bin/activate
pip install numpy scipy matplotlib
python besserwisser_fig1.py
python besserwisser_fig2.py
```

`besserwisser_fig1.py` writes both `fig1_theory.pdf` and `fig2_stuckness.pdf`. Running `besserwisser_fig2.py` afterwards replaces `fig2_stuckness.pdf` with its own version. The figures illustrate the paper's models; they are not empirical measurements.

## Citation

```bibtex
@article{vosteen2026besserwisser,
  title  = {The Besserwisser Effect: A Complexity-Theoretic Proof that
            Criticism Cannot Substitute for Production},
  author = {Vosteen, Hakvin},
  year   = {2026},
  url    = {https://github.com/hakvinv/besserwisser-effect}
}
```

The paper is presented under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
