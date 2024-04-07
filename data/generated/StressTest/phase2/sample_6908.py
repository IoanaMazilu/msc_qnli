# Premise: City A to city B, Andrew drove for 1 hr at 44 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for less than 1 hr at 44 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

drive_time_at_44mph_premise = 1
drive_time_at_44mph_hypothesis = 1
drive_time_at_60mph_premise = 3
drive_time_at_60mph_hypothesis = 3

# the hypothesis refers to the driving times at speeds mentioned in the premise
if drive_time_at_44mph_hypothesis >= drive_time_at_44mph_premise:
    # check if the driving time at 44 mph in the hypothesis contradicts the driving time at 44 mph in the premise
    label = "contradiction"
elif drive_time_at_60mph_hypothesis != drive_time_at_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

