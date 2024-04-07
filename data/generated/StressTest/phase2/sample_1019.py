# Premise: John has 4 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Hypothesis: John has 2 friends who want to ride in his new car that can accommodate only 3 people at a time (John plus 2 passengers)
# Golden Label: contradiction

friends_premise = 4
friends_hypothesis = 2
car_capacity = 3

# the hypothesis refers to the number of friends John has and who want to ride in his new car, mentioned also in the premise
if friends_hypothesis > car_capacity:
    # check if the number of friends in the hypothesis contradicts the car's capacity
    label = "contradiction"
elif friends_hypothesis > friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

