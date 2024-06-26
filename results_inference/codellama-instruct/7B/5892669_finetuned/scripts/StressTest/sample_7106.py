hours_paid_x_premise = 30
hours_paid_x_hypothesis = 30
additional_hours_paid_2x_premise = 2
additional_hours_paid_2x_hypothesis = 2

# the hypothesis refers to the number of hours Harry is paid x dollars per hour and the number of additional hours he is paid 2x dollars per hour
if hours_paid_x_hypothesis >= hours_paid_x_premise:
    # check if the number of hours Harry is paid x dollars per hour in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif additional_hours_paid_2x_hypothesis!= additional_hours_paid_2x_premise:
    # check if the number of additional hours Harry is paid 2x dollars per hour in the hypothesis contradicts the number of additional hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
