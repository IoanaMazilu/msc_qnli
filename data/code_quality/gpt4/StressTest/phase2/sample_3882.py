hours_spent_premise = 3
hours_spent_hypothesis = 4

# the hypothesis refers to the number of hours Aaron spent jogging and walking from the premise
if hours_spent_hypothesis < hours_spent_premise:
    # check if the estimate of 'hours_spent_hypothesis' contradicts the number of hours in the premise
    label = "contradiction"
elif hours_spent_hypothesis > hours_spent_premise:
    # the premise gives only an exact number for the hours spent
    # any number of hours greater than 'hours_spent_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
