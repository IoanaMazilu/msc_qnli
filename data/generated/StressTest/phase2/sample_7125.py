# Premise: How many miles from home can Aaron jog so that he spends a total of 3 hours jogging and walking?
# Hypothesis: How many miles from home can Aaron jog so that he spends a total of more than 1 hours jogging and walking?
# Golden Label: entailment

total_hours_premise = 3
total_hours_hypothesis = 1

# the hypothesis refers to the total jogging and walking hours mentioned in the premise
if total_hours_hypothesis >= total_hours_premise:
    # check if the estimate of 'total_hours_hypothesis' contradicts the total hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

