# Define variables for the numerical entities in the premise and hypothesis
rahul_age_premise = 26
deepak_age_premise = 26
rahul_deepak_ratio_premise = 8/2

# Define variables for the numerical entities in the hypothesis
rahul_age_hypothesis = 26
deepak_age_hypothesis = 26
rahul_deepak_ratio_hypothesis = 5/2

# Check if the ratio in the hypothesis contradicts the ratio in the premise
if rahul_deepak_ratio_hypothesis!= rahul_deepak_ratio_premise:
    label = "contradiction"
# Check if the age in the hypothesis contradicts the age in the premise
elif rahul_age_hypothesis!= rahul_age_premise:
    label = "contradiction"
# If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
else:
    label = "entailment"

print(label)
