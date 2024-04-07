# Premise: City A to city B, Andrew drove for 1 hr at 50 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for less than 7 hr at 50 mph and for 3 hours at 60 mph.
# Golden Label: entailment

drive_time_50mph_premise = 1
drive_time_50mph_hypothesis = 7
drive_time_60mph_premise = 3
drive_time_60mph_hypothesis = 3

# the hypothesis refers to the driving times at 50mph and 60mph mentioned in the premise
if drive_time_50mph_hypothesis <= drive_time_50mph_premise:
    # check if the estimate of 'drive_time_50mph_hypothesis' contradicts the driving time at 50mph in the premise
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if the driving time at 60mph in the hypothesis contradicts the driving time at 60mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

