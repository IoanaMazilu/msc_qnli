without_shelter_premise = 50000
without_shelter_hypothesis = 50000

# the hypothesis mentions the number of people without shelter, which is also referenced in the premise
if without_shelter_hypothesis!= without_shelter_premise:
    # check if the number of people without shelter in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of people without shelter in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
