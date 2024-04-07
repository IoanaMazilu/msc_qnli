# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him 1 months later, investing Rs.
# Golden Label: contradiction

joining_time_premise = 2
joining_time_hypothesis = 1

# the hypothesis talks about the time Jose joined, which is also referenced in the premise
if joining_time_hypothesis != joining_time_premise:
    # check if the joining time in the hypothesis contradicts the joining time mentioned in the premise
    label = "contradiction"
else:
    # if the joining time in the hypothesis does not contradict the joining time in the premise, we can infer entailment
    label = "entailment"

print(label)

