# Define variables for the premise and hypothesis
num_people_premise = 2
num_people_hypothesis = 5

# Check if the hypothesis value contradicts the premise
if num_people_hypothesis <= num_people_premise:
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise value, so the hypothesis is entailed
    label = "entailment"

print(label)
