car_owners_percentage_premise = 25
car_owners_percentage_hypothesis = 35

# the hypothesis refers to the percentage of students owning cars at Morse, which is also mentioned in the premise
if car_owners_percentage_hypothesis <= car_owners_percentage_premise:
    # check if the hypothesis value contradicts the percentage of students owning cars in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)