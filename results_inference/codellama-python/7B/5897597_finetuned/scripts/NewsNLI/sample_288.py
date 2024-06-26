people_without_shelter_premise = 50000
people_without_shelter_hypothesis = 50000

# the hypothesis mentions the number of people without shelter in Italy, which is also mentioned in the premise
if people_without_shelter_hypothesis!= people_without_shelter_premise:
    # check if the number of people without shelter in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
