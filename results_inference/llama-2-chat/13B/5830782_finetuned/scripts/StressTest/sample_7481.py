first_hours_premise = 24
additional_hours_premise = 1.5
first_hours_hypothesis = 54
additional_hours_hypothesis = 1.5

# the hypothesis refers to the number of hours Harry is paid x dollars and the additional hours paid 1.5 x
if first_hours_premise!= first_hours_hypothesis:
    # check if the number of hours Harry is paid x dollars in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif additional_hours_premise!= additional_hours_hypothesis:
    # check if the rate for additional hours in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
