# Premise: If the distance between their homes is 50 kilometers, Maxwell's walking speed is 3 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Hypothesis: If the distance between their homes is more than 50 kilometers, Maxwell's walking speed is 3 km/h, and Brad's running speed is 6 km/h, what is the distance traveled by Brad?
# Golden Label: contradiction

distance_premise = 50
distance_hypothesis = 50

# the hypothesis refers to the distance between the homes mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

