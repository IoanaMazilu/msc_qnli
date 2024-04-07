# Premise: City A to city B, Andrew drove for 1 hr at 40 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for more than 1 hr at 40 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

drive_time_40mph_premise = 1
drive_time_40mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving times at different speeds mentioned in the premise
if drive_time_40mph_hypothesis < drive_time_40mph_premise:
    # check if the hypothesis estimate contradicts the driving time at 40 mph in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph reported in the premise
    label = "contradiction"
else:
    # the premise gives exact figures for the driving times
    # any driving time at 40 mph greater than 'drive_time_40mph_premise' cannot be entailed from the premise
    label = "neutral"

print(label)

