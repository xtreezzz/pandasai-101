import pandas as pd
import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Define the number of samples
n_samples = 300

# Define the underlying factors (latent variables)
# Factor 1: General Intelligence/Verbal Ability
f1 = np.random.normal(0, 1, n_samples)
# Factor 2: Mathematical/Spatial Ability
f2 = np.random.normal(0, 1, n_samples)
# Factor 3: Speed/Attention
f3 = np.random.normal(0, 1, n_samples)

# Define the observed variables (manifest variables) as a linear combination of factors + error
# V1: Vocabulary (loads heavily on F1)
v1 = 0.8 * f1 + 0.1 * f2 + np.random.normal(0, 0.5, n_samples)
# V2: Reading Comprehension (loads heavily on F1)
v2 = 0.7 * f1 + 0.2 * f3 + np.random.normal(0, 0.6, n_samples)
# V3: Arithmetic (loads heavily on F2)
v3 = 0.1 * f1 + 0.9 * f2 + np.random.normal(0, 0.4, n_samples)
# V4: Spatial Reasoning (loads heavily on F2)
v4 = 0.2 * f1 + 0.7 * f2 + np.random.normal(0, 0.5, n_samples)
# V5: Reaction Time (loads heavily on F3, negative correlation)
v5 = -0.1 * f1 + 0.1 * f2 - 0.8 * f3 + np.random.normal(0, 0.5, n_samples)
# V6: Attention Span (loads heavily on F3)
v6 = 0.1 * f1 + 0.1 * f2 + 0.6 * f3 + np.random.normal(0, 0.6, n_samples)

# Create the DataFrame
data = pd.DataFrame({
    'Vocabulary': v1,
    'Reading_Comp': v2,
    'Arithmetic': v3,
    'Spatial_Reasoning': v4,
    'Reaction_Time': v5,
    'Attention_Span': v6
})

# Scale the data to be more like real-world test scores (e.g., mean 100, std 15)
data = (data - data.mean()) / data.std() * 15 + 100

# Save the data to a CSV file
data.to_csv('psychometric_data.csv', index=False)

print("Synthetic psychometric_data.csv created successfully.")
