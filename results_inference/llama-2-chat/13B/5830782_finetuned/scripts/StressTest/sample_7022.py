car_owners_percentage_premise = 20
car_owners_percentage_hypothesis = 50

# the hypothesis refers to the percentage of students owning cars at Morse, which is also mentioned in the premise
if car_owners_percentage_hypothesis!= car_owners_percentage_premise:
    # check if the car ownership percentage in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # if the car ownership percentages in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)