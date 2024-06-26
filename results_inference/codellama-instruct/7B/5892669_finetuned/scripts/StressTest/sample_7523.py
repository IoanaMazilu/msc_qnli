friends_premise = 6
friends_hypothesis = 5
car_capacity_premise = 5
car_capacity_hypothesis = 5

# the hypothesis refers to the number of John's friends and the car's capacity mentioned in the premise
if friends_premise!= friends_hypothesis:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
elif car_capacity_premise!= car_capacity_hypothesis:
    # check if the car's capacity in the hypothesis contradicts the car's capacity reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
