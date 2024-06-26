first_hours_premise = 21
first_hours_hypothesis = 11

# the hypothesis refers to the number of hours Harry is paid x dollars per hour, which is also mentioned in the premise
if first_hours_hypothesis > first_hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the number of hours in the hypothesis does not contradict the number of hours in the premise, we can infer entailment
    label = "entailment"

print(label)
