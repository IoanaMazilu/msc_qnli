# Define variables for the premise and hypothesis
age_sameer_premise = 5
age_anand_premise = 4
age_sameer_hypothesis = 5
age_anand_hypothesis = 4

# Check if the ratio of the ages in the hypothesis is less than the ratio in the premise
if age_sameer_hypothesis / age_anand_hypothesis < age_sameer_premise / age_anand_premise:
    # The hypothesis is entailed from the premise
    label = "entailment"
else:
    # The hypothesis is not entailed from the premise
    label = "contradiction"

print(label)
