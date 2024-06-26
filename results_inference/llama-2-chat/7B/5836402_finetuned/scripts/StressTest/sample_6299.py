first_12_hours_pay_premise = 1.5 * 12
first_12_hours_pay_hypothesis = 52

# the hypothesis refers to the number of hours Harry is paid for in a week, as stated in the premise
if first_12_hours_pay_premise!= first_12_hours_pay_hypothesis:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
