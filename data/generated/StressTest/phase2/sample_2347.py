# Premise: Ratio between Rahul and Deepak is less than 5:3, After 6 Years Rahul age will be 42 years.
# Hypothesis: Ratio between Rahul and Deepak is 4:3, After 6 Years Rahul age will be 42 years.
# Golden Label: neutral

# Variables for the premise
ratio_rahul_deepak_premise = 5/3
rahul_age_in_6_years_premise = 42

# Variables for the hypothesis
ratio_rahul_deepak_hypothesis = 4/3
rahul_age_in_6_years_hypothesis = 42

# Compare the values
if ratio_rahul_deepak_hypothesis >= ratio_rahul_deepak_premise:
    # check if the ratio in the hypothesis contradicts the premise
    label = "contradiction"
elif rahul_age_in_6_years_hypothesis != rahul_age_in_6_years_premise:
    # check if Rahul's future age in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

