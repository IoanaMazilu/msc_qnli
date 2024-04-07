# Premise: City A to city B, John drove for 1 hour at 40 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, John drove for less than 5 hour at 40 mph and for 3 hours at 60 mph.
# Golden Label: entailment

driving_time_at_40mph_premise = 1
driving_time_at_40mph_hypothesis = 5
driving_time_at_60mph_premise = 3
driving_time_at_60mph_hypothesis = 3

# the hypothesis specifies the time John drove at certain speeds, which are also referenced in the premise
if driving_time_at_40mph_hypothesis <= driving_time_at_40mph_premise:
    # check if the hypothesis value contradicts the driving time at 40mph in the premise
    label = "contradiction"
elif driving_time_at_60mph_hypothesis != driving_time_at_60mph_premise:
    # check if the driving time at 60mph in the hypothesis contradicts the driving time at 60mph in the premise
    label = "contradiction"
else:
    # the premise gives exact values for the driving times
    # if the hypothesis values are consistent with the premise but not exact, we infer neutrality
    label = "neutral"

print(label)

