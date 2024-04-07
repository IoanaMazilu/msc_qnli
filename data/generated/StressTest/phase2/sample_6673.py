# Premise: City A to city B, Andrew drove for less than 5 hr at 40 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for 1 hr at 40 mph and for 3 hours at 60 mph.
# Golden Label: neutral

drive_time_40mph_premise = 5
drive_time_40mph_hypothesis = 1
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving times at certain speeds mentioned in the premise
if drive_time_40mph_hypothesis >= drive_time_40mph_premise:
    # check if the estimate of 'drive_time_40mph_hypothesis' contradicts the fact that the driving time at 40mph in the premise was less than 'drive_time_40mph_premise'
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if the driving time at 60mph in the hypothesis contradicts the driving time at 60mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

