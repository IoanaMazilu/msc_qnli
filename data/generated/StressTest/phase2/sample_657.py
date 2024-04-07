# Premise: Mary can do a piece of work in 28 days.
# Hypothesis: Mary can do a piece of work in less than 38 days.
# Golden Label: entailment

work_duration_premise = 28
work_duration_hypothesis = 38

# the hypothesis refers to the duration Mary can finish a piece of work, which is also mentioned in the premise
if work_duration_premise > work_duration_hypothesis:
    # check if the time in the premise contradicts the estimate of less than 'work_duration_hypothesis' in the hypothesis
    label = "contradiction"
elif work_duration_premise < work_duration_hypothesis:
    # if the time in the premise is less than 'work_duration_hypothesis', it can be inferred from the hypothesis
    label = "entailment"
else:
    # if the time values are equal, it doesn't contradict the hypothesis but cannot be fully entailed from it either
    label = "neutral"

print(label)

