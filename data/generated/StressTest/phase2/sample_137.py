# Premise: Jose joined him 2 months later, investing Rs.
# Hypothesis: Jose joined him 8 months later, investing Rs.
# Golden Label: contradiction

joining_time_premise = 2
joining_time_hypothesis = 8

# the hypothesis talks about the time when Jose joined, referenced also in the premise
if joining_time_hypothesis != joining_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

