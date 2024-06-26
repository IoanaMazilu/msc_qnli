distance_traveled_premise = 240
distance_traveled_hypothesis = 340

# the hypothesis refers to the distance traveled on the first day of Louisa's vacation
if distance_traveled_hypothesis <= distance_traveled_premise:
    # check if the estimate of 'distance_traveled_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
