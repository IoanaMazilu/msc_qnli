# Define variables for the premise and hypothesis
num_boys_premise = 300
num_girls_premise = 240
num_boys_hypothesis = 400
num_girls_hypothesis = 240

# Check if the hypothesis values contradict the premise
if num_boys_hypothesis > num_boys_premise:
    label = "contradiction"
elif num_girls_hypothesis > num_girls_premise:
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
