car_owners_premise = 20
car_owners_hypothesis = 50

# the hypothesis refers to the percentage of students owning cars at Morse, also mentioned in the premise
if car_owners_hypothesis!= car_owners_premise:
    # check if the percentage of students owning cars in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
