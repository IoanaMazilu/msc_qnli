fishbowls_premise = 261.0
fish_per_fishbowl_premise = 23.0
total_fish_premise = fishbowls_premise * fish_per_fishbowl_premise
hypothesis_fish = 6003.0

# The hypothesis refers to the total number of fish, which is also mentioned in the premise
# Compute the total number of fish in the premise
total_fish_hypothesis = fishbowls_premise * fish_per_fishbowl_premise

# Check if the hypothesis value contradicts the premise value
if total_fish_hypothesis!= total_fish_premise:
    label = "contradiction"
else:
    # If the hypothesis value and estimate do not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
