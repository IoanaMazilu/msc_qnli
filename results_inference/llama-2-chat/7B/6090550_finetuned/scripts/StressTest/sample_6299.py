first_hours_pay_premise = 12
first_hours_pay_hypothesis = 52
additional_hours_pay_premise = 1.5 * x
additional_hours_pay_hypothesis = 1.5 * x

# the hypothesis refers to the pay for the first hours and the additional hours worked
if first_hours_pay_premise!= first_hours_pay_hypothesis:
    # check if the number of hours paid for in the first hours in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif additional_hours_pay_premise!= additional_hours_pay_hypothesis:
    # check if the additional hours pay in the hypothesis contradicts the additional hours pay in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
