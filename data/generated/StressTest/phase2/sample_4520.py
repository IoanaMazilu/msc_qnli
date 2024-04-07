# Premise: The distance between their homes is 45 kilometers, Cara's walking speed is 6 km/h, and Don's walking speed is 5 km/h.
# Hypothesis: The distance between their homes is 75 kilometers, Cara's walking speed is 6 km/h, and Don's walking speed is 5 km/h.
# Golden Label: contradiction

distance_homes_premise = 45
distance_homes_hypothesis = 75
cara_speed_premise = 6
cara_speed_hypothesis = 6
don_speed_premise = 5
don_speed_hypothesis = 5

# the hypothesis talks about the distance between their homes and their walking speeds, same as in the premise
if distance_homes_hypothesis != distance_homes_premise:
    # check if the distance between their homes in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif cara_speed_hypothesis != cara_speed_premise:
    # check if Cara's walking speed in the hypothesis contradicts her walking speed in the premise
    label = "contradiction"
elif don_speed_hypothesis != don_speed_premise:
    # check if Don's walking speed in the hypothesis contradicts his walking speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

