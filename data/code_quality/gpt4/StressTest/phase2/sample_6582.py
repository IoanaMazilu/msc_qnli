people_premise = 5
people_hypothesis = 2

# the hypothesis refers to the number of people mentioned in the premise
if people_premise <= people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people seated in the premise
    label = "contradiction"
elif people_hypothesis != people_premise:
    # the premise gives specific details about the number of people
    # any number of people greater than 'people_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
