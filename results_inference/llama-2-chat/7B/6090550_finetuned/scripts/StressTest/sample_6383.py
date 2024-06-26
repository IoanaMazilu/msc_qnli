first_hours_pay_premise = 40
first_hours_pay_hypothesis = 50
additional_hours_pay_premise = 2 * x
additional_hours_pay_hypothesis = 2 * x

# the hypothesis talks about the pay for the first and additional hours worked, which are also mentioned in the premise
if first_hours_pay_hypothesis!= first_hours_pay_premise:
    # check if the number of hours paid in the first hours in the hypothesis contradicts the number of hours paid in the premise
    label = "contradiction"
elif additional_hours_pay_hypothesis!= additional_hours_pay_premise:
    # check if the additional hours pay in the hypothesis contradicts the additional hours pay in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
