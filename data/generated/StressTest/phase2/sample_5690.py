# Premise: When they are at a distance of 50 miles, a housefly starts flying from Suresh Raina's cycle towards Gautam Gambhir at a relative speed of 17 miles per hour with respect to Raina's speed.
# Hypothesis: When they are at a distance of 80 miles, a housefly starts flying from Suresh Raina's cycle towards Gautam Gambhir at a relative speed of 17 miles per hour with respect to Raina's speed.
# Golden Label: contradiction

distance_premise = 50
distance_hypothesis = 80

relative_speed_premise = 17
relative_speed_hypothesis = 17

# the hypothesis talks about the distance and relative speed of the housefly, which is also mentioned in the premise
if distance_hypothesis != distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif relative_speed_hypothesis != relative_speed_premise:
    # check if the relative speed in the hypothesis contradicts the relative speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

