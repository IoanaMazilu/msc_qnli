# define variables for the premise and hypothesis
first_hours_premise = 40
first_hours_hypothesis = 30
additional_pay_premise = 2
additional_pay_hypothesis = 2

# the hypothesis refers to the number of hours and the pay rate mentioned in the premise
if first_hours_premise < first_hours_hypothesis:
    # check if the number of initial hours in the hypothesis contradicts the number of initial hours in the premise
    label = "contradiction"
elif additional_pay_hypothesis != additional_pay_premise:
    # check if the pay rate for additional hours in the hypothesis contradicts the pay rate for additional hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
