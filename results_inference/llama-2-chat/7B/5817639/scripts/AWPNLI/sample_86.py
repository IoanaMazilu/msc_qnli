# Define variables for the premise and hypothesis
box_caps_premise = float(7.0)
box_caps_hypothesis = float(14.0)

# Compare the number of bottle caps in the hypothesis to the premise
if box_caps_hypothesis >= box_caps_premise:
    # If the number of bottle caps in the hypothesis is greater than or equal to the number of bottle caps in the premise, it is an entailment
    label = "entailment"
elif box_caps_hypothesis - box_caps_premise > 0:
    # If the number of bottle caps in the hypothesis is less than the number of bottle caps in the premise, it is a contradiction
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
