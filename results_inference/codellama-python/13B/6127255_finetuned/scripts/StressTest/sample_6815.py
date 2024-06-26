car_owners_percentage_premise = 18
car_owners_percentage_hypothesis = 58

# the hypothesis refers to the percentage of students owning cars at Morse, also mentioned in the premise
if car_owners_percentage_hypothesis!= car_owners_percentage_premise:
    # check if the percentage of students owning cars in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
