# Premise: City A to city B, Andrew drove for less than 5 hr at 48 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for 1 hr at 48 mph and for 3 hours at 60 mph.
# Golden Label: neutral

driving_time_48mph_premise = 5
driving_time_48mph_hypothesis = 1
driving_time_60mph_premise = 3
driving_time_60mph_hypothesis = 3

# the hypothesis talks about the driving time at certain speeds between two cities mentioned also in the premise
if driving_time_48mph_hypothesis >= driving_time_48mph_premise:
    # check if the driving time at 48 mph in the hypothesis contradicts the estimate of less than 'driving_time_48mph_premise' in the premise
    label = "contradiction"
elif driving_time_60mph_hypothesis != driving_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the driving time at 48 mph
    # any driving time less than 'driving_time_48mph_premise' at 48 mph is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

