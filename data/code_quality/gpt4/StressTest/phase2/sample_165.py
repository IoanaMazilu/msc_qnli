people_premise = 7
people_hypothesis = 1

# the hypothesis refers to the number of people that can be seated on a bench, which is also mentioned in the premise
if people_premise <= people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
elif people_hypothesis != people_premise:
    # the premise gives a specific number of people, any number different from 'people_premise' cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
