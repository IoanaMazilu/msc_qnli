# Premise: John takes a trip and drives 9 hours from Town X to Town Z at a rate of 60 miles per hour.
# Hypothesis: John takes a trip and drives more than 4 hours from Town X to Town Z at a rate of 60 miles per hour.
# Golden Label: entailment

driving_hours_premise = 9
driving_hours_hypothesis = 4
driving_speed_premise = 60
driving_speed_hypothesis = 60

# the hypothesis refers to the driving time and speed mentioned in the premise
if driving_hours_hypothesis >= driving_hours_premise:
    # check if the estimate of 'driving_hours_hypothesis' contradicts the driving time in the premise
    label = "contradiction"
elif driving_speed_hypothesis != driving_speed_premise:
    # check if the driving speed in the hypothesis contradicts the driving speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

