hours_regular_pay_premise = 30
hours_regular_pay_hypothesis = 80

# the hypothesis talks about the number of hours Harry works on regular pay, referenced also in the premise
if hours_regular_pay_hypothesis != hours_regular_pay_premise:
    # check if the number of hours worked on regular pay in the hypothesis contradicts the number of hours worked on regular pay reported in the premise
    label = "contradiction"
else:
    # if the number of hours worked on regular pay in the hypothesis does not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
