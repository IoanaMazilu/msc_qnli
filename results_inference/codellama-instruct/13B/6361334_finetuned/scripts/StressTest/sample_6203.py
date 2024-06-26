distance_traveled_premise = 200
distance_traveled_hypothesis = 200

# the hypothesis refers to the distance traveled on the first day of Louisa's vacation
# the premise mentions the distance traveled on the first day of her vacation
if distance_traveled_hypothesis <= distance_traveled_premise:
    # check if the estimate of 'distance_traveled_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
