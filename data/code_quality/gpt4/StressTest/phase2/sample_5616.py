people_premise = 8
people_hypothesis = 1

# the hypothesis refers to the seating arrangement of people, mentioned also in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis contradicts the number of people mentioned in the premise
    label = "contradiction"
elif people_hypothesis != people_premise - 1:
    # the premise gives the exact number of people
    # any number of people other than 'people_premise - 1' cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
