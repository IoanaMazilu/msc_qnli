x_dollars_premise = 0
x_dollars_hypothesis = 2
hours_worked_premise = 80
hours_worked_hypothesis = 30

# the hypothesis refers to the pay rate and number of hours worked in the premise
if hours_worked_hypothesis >= hours_worked_premise:
    # check if the hypothesis estimate contradicts the number of hours worked in the premise
    label = "contradiction"
elif x_dollars_hypothesis!= x_dollars_premise:
    # check if the pay rate in the hypothesis contradicts the pay rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
