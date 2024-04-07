# Premise: After they have worked together for 12 days peter stops and Peter completes the remaining work in 10 days.
# Hypothesis: After they have worked together for less than 32 days peter stops and Peter completes the remaining work in 10 days.
# Golden Label: entailment

work_together_premise = 12
work_together_hypothesis = 32
remaining_work_premise = 10
remaining_work_hypothesis = 10

# the hypothesis refers to the number of days they worked together and the remaining work that Peter completes, mentioned in the premise
if work_together_hypothesis < work_together_premise:
    # check if the 'work_together_hypothesis' contradicts the number of days worked together in the premise
    label = "contradiction"
elif remaining_work_hypothesis != remaining_work_premise:
    # check if the number of remaining work days in the hypothesis contradicts the number of remaining work days reported in the premise
    label = "contradiction"
elif work_together_hypothesis > work_together_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

