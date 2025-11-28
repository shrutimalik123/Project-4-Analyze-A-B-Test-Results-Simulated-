# Project-4-Analyze-A-B-Test-Results-Simulated-

Project 4: Analyze A/B Test Results (Simulated)

Objective

The goal is to simulate an A/B test scenario where a company is deciding whether to launch a new webpage (the Treatment group) or keep the old one (the Control group). We will use statistical methods to determine if the new page leads to a significant difference in conversion rate.

## Installation

To run this project, you need to install the following Python libraries:

```bash
pip install pandas scipy numpy statsmodels
```

## Usage

Run the simulation script using Python:

```bash
python ab_test_simulation.py
```

## Results Explanation

The script simulates user conversions for two groups:
- **Control Group**: Users seeing the old page.
- **Treatment Group**: Users seeing the new page.

It then performs a **Two-Sample Z-Test** for proportions to check if the observed difference in conversion rates is statistically significant.

### Key Metrics:
- **Z-Statistic**: Measures how many standard deviations the observed difference is from the null hypothesis (no difference).
- **P-Value**: The probability of observing such a difference (or more extreme) assuming the null hypothesis is true.

### Decision Rule:
- We use a significance level ($\alpha$) of **0.05**.
- **If p-value < 0.05**: We reject the Null Hypothesis. The result is statistically significant, and we recommend launching the new page.
- **If p-value >= 0.05**: We fail to reject the Null Hypothesis. The result is not statistically significant, and we recommend keeping the old page or gathering more data.
