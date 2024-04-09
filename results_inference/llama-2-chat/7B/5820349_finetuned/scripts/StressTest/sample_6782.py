first_hours_premise = 30
first_hours_hypothesis = 80

# the hypothesis refers to the number of hours Harry is paid x dollars per hour, mentioned in the premise
if first_hours_hypothesis!= first_hours_premise:
    # check if the number of hours in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
