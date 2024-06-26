injured_premise = 1500
shelter_premise = 50000

hypothesis_shelter = 50000

# the hypothesis mentions the number of people without shelter, which is also mentioned in the premise
if shelter_hypothesis!= shelter_premise:
    # check if the number of people without shelter in the hypothesis contradicts the number of people without shelter in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
