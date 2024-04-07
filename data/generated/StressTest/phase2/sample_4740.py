# Premise: If the distance between their homes is 50 kilometers, Maxwell's walking speed is 3 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is less than 80 kilometers, Maxwell's walking speed is 3 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: entailment

distance_premise = 50
distance_hypothesis = 80

# the hypothesis refers to the distance between the homes mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis estimate contradicts the exact distance given in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # check if the hypothesis estimate contradicts the exact distance given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

