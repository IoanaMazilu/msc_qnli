# Define variables for the premise and hypothesis
age_sameer_premise = 3
age_anand_premise = 4
age_sameer_hypothesis = 5
age_anand_hypothesis = 4

# Check if the ratio of the ages in the hypothesis contradicts the ratio in the premise
if age_sameer_hypothesis / age_anand_hypothesis!= age_sameer_premise / age_anand_premise:
    label = "contradiction"
else:
    # If the ratio of the ages in the hypothesis is consistent with the ratio in the premise, we can infer entailment
    label = "entailment"

print(label)
