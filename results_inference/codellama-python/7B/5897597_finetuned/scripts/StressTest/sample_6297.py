first_hours_premise = 12
first_hours_hypothesis = 82

# the hypothesis refers to the number of hours Harry is paid x dollars per hour, as mentioned in the premise
if first_hours_hypothesis <= first_hours_premise:
    # check if the hypothesis value contradicts the number of hours in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
