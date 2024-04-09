car_owners_percentage_premise = 25
car_owners_percentage_hypothesis = 85

# the hypothesis refers to the percentage of students owning cars at Morse, which is also mentioned in the premise
if car_owners_percentage_premise!= car_owners_percentage_hypothesis:
    # check if the percentage of car owners in the hypothesis contradicts the percentage of car owners in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise percentage, we can infer entailment
    label = "entailment"

print(label)
