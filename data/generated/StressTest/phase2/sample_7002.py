# Premise: They both work together for 5 days and then Sushil goes away.
# Hypothesis: They both work together for more than 3 days and then Sushil goes away.
# Golden Label: entailment

work_days_premise = 5
work_days_hypothesis = 3

# the hypothesis refers to the number of days they worked together, which is also mentioned in the premise
if work_days_premise < work_days_hypothesis:
    # check if the number of work days in the premise contradicts the estimate of more than 'work_days_hypothesis'
    label = "contradiction"
elif work_days_premise == work_days_hypothesis:
    # check if the number of work days in the premise is the same as the number in the hypothesis
    label = "neutral"
else:
    # if the number of work days in the premise is larger than the number in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

