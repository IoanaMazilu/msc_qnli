car_owners_percentage_premise = 18
car_owners_percentage_hypothesis = 58

# the hypothesis refers to the percentage of students owning cars at Morse, mentioned in the premise
if car_owners_percentage_premise!= car_owners_percentage_hypothesis:
    # check if the percentage of car owners in the hypothesis contradicts the percentage of car owners in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
