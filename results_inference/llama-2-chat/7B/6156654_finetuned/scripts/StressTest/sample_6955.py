# Define the premise and hypothesis variables
premise = 80
hypothesis = 40

# The hypothesis refers to the number of shirts each person has after purchasing 8 shirts each
if premise < hypothesis:
    # Check if the number of shirts in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # If the number of shirts in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
