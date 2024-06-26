# defining variables for the premise and hypothesis
x_per_hour_premise = 0
x_per_hour_hypothesis = 0
hours_worked_premise = 40
hours_worked_hypothesis = 40

# the hypothesis refers to the number of hours worked and the pay per hour, which are also mentioned in the premise
if hours_worked_hypothesis >= hours_worked_premise:
    # check if the hypothesis estimate contradicts the number of hours worked in the premise
    label = "contradiction"
elif x_per_hour_hypothesis!= x_per_hour_premise:
    # check if the pay per hour in the hypothesis contradicts the pay per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
