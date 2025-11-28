import pandas as pd
from scipy import stats
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

# A/B Test Parameters (Simulated)
N_control = 10000  # Number of users in Control group
N_treatment = 10000  # Number of users in Treatment group
p_control = 0.12   # True conversion rate for Control (Old Page)
p_new_observed = 0.125 # Observed conversion rate for Treatment (New Page)

# Simulate conversions (1 for converted, 0 for not converted)
# Control group: Uses the true p_control rate
control_conversions = np.random.binomial(n=1, p=p_control, size=N_control)

# Treatment group: Uses a slightly higher rate to simulate observed results
treatment_conversions = np.random.binomial(n=1, p=p_new_observed, size=N_treatment)

# Create a DataFrame for analysis
df_ab = pd.DataFrame({
    'group': ['Control'] * N_control + ['Treatment'] * N_treatment,
    'converted': np.concatenate([control_conversions, treatment_conversions])
})

# Calculate observed conversion rates
control_cr = df_ab[df_ab['group'] == 'Control']['converted'].mean()
treatment_cr = df_ab[df_ab['group'] == 'Treatment']['converted'].mean()

print(f"Control Conversion Rate: {control_cr:.4f}")
print(f"Treatment Conversion Rate: {treatment_cr:.4f}")

# Count successes (conversions) and sample sizes (total users)
count = np.array([df_ab[df_ab['group'] == 'Treatment']['converted'].sum(),
                  df_ab[df_ab['group'] == 'Control']['converted'].sum()])
nobs = np.array([N_treatment, N_control])

# Perform the Z-test (one-tailed test since we hypothesize p_new > p_old)
# 'smaller' means H_A: proportion_1 > proportion_2 (our goal)
z_stat, p_value = proportions_ztest(count, nobs, alternative='larger')

print("\n--- A/B Test (Two-Sample Z-Test) Results ---")
print(f"Z-Statistic: {z_stat:.4f}")
print(f"P-Value: {p_value:.4f}")

alpha = 0.05

if p_value < alpha:
    recommendation = "Reject the Null Hypothesis. The new page has a statistically significant higher conversion rate. **Recommendation: Launch the new webpage.**"
else:
    recommendation = "Fail to Reject the Null Hypothesis. The difference in conversion rates is not statistically significant. **Recommendation: Keep the old webpage or gather more data.**"

print("\n--- Final Recommendation (at α = 0.05) ---")
print(recommendation)
