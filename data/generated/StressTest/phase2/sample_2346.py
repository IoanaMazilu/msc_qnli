# Premise: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 42 years.
# Hypothesis: Ratio between Rahul and Deepak is less than 5:3, After 6 Years Rahul age will be 42 years.
# Golden Label: entailment

# Defining variables for the premise and hypothesis
rahul_deepak_ratio_premise = 4 / 3
rahul_deepak_ratio_hypothesis = 5 / 3
rahul_age_future_premise = 42
rahul_age_future_hypothesis = 42

# Checking if the ratio between Rahul and Deepak in the hypothesis is less than that in the premise
if rahul_deepak_ratio_hypothesis >= rahul_deepak_ratio_premise:
    # If the ratio in the hypothesis is equal to or greater than the ratio in the premise, it's a contradiction
    label = "contradiction"
elif rahul_age_future_hypothesis != rahul_age_future_premise:
    # If the future ages of Rahul in the premise and hypothesis do not match, it's a contradiction
    label = "contradiction"
else:
    # If neither of the above conditions are met, the hypothesis is entailed by the premise
    label = "entailment"

print(label)

