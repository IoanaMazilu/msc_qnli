# Premise: They both work together for less than 8 days and then Sushil goes away.
# Hypothesis: They both work together for 5 days and then Sushil goes away.
# Golden Label: neutral

work_days_premise = 8
work_days_hypothesis = 5

# the hypothesis refers to the number of days they both work together mentioned in the premise
if work_days_hypothesis > work_days_premise:
    # check if the number of 'work_days_hypothesis' contradicts the estimated less than 'work_days_premise'
    label = "contradiction"
elif work_days_hypothesis <= work_days_premise:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

