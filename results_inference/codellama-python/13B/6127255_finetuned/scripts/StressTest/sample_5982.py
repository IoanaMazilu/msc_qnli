car_owners_premise = 25
car_owners_hypothesis = 35

# the hypothesis refers to the percentage of students owning cars at Morse, also mentioned in the premise
if car_owners_hypothesis <= car_owners_premise:
    # check if the estimate of 'car_owners_hypothesis' contradicts the percentage of car owners in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
