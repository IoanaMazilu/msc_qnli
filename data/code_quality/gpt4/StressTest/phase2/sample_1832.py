distance_premise = 100  # defined in centimeters
step_length_premise = 20  # defined in centimeters
distance_hypothesis = 100  # defined in centimeters
step_length_hypothesis = 60  # defined in centimeters

# the hypothesis talks about the distance to the butcher's shop and the length of Mary's steps, both mentioned in the premise
if step_length_hypothesis != step_length_premise:
    # check if the step length in the hypothesis contradicts the step length reported in the premise
    label = "contradiction"
elif distance_hypothesis != distance_premise:
    # check if the distance to the butcher's shop in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
