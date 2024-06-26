hours_worked_james_premise = 45
hours_worked_james_hypothesis = 55

# the hypothesis refers to the number of hours James worked, mentioned in the premise
if hours_worked_james_hypothesis <= hours_worked_james_premise:
    # check if the estimate of 'hours_worked_james_hypothesis' contradicts the number of hours James worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)