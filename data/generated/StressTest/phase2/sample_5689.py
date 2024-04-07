# Premise: When they are at a distance of less than 60 miles, a housefly starts flying from Suresh Raina's cycle towards Gautam Gambhir at a relative speed of 17 miles per hour with respect to Raina's speed.
# Hypothesis: When they are at a distance of 50 miles, a housefly starts flying from Suresh Raina's cycle towards Gautam Gambhir at a relative speed of 17 miles per hour with respect to Raina's speed.
# Golden Label: neutral

distance_premise = 60
distance_hypothesis = 50
relative_speed_premise = 17
relative_speed_hypothesis = 17

# the hypothesis talks about the same situation described in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif relative_speed_hypothesis != relative_speed_premise:
    # check if the relative speed mentioned in the hypothesis contradicts the one mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

