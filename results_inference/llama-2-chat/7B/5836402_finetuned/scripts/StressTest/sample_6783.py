first_hours_premise = 40
first_hours_hypothesis = 70
multiplier_premise = 1.5
multiplier_hypothesis = 1.5

# the hypothesis refers to the number of hours worked per week and the pay rate for each hour
if first_hours_hypothesis >= first_hours_premise:
    # check if the estimate of 'first_hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
elif multiplier_hypothesis!= multiplier_premise:
    # check if the pay rate for each additional hour in the hypothesis contradicts the pay rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
