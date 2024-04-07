# Premise: James took a 3-hour bike ride.
# Hypothesis: James took a less than 4-hour bike ride.
# Golden Label: entailment

ride_duration_premise = 3
ride_duration_hypothesis = 4

# the hypothesis refers to the duration of James's bike ride mentioned in the premise
if ride_duration_premise > ride_duration_hypothesis:
    # check if the 'ride_duration_premise' contradicts the hypothesis that the bike ride was less than 4 hours
    label = "contradiction"
elif ride_duration_hypothesis > ride_duration_premise:
    # check if the 'ride_duration_hypothesis' is more than the actual bike ride duration in the premise
    # if it is, then it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the 'ride_duration_hypothesis' does not contradict the 'ride_duration_premise', we can infer entailment
    label = "entailment"

print(label)

