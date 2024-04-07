# Premise: City A to city B, Andrew drove for less than 7 hr at 50 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for 1 hr at 50 mph and for 3 hours at 60 mph.
# Golden Label: neutral

drive_time_at_50mph_premise = 7
drive_time_at_50mph_hypothesis = 1
drive_time_at_60mph_premise = 3
drive_time_at_60mph_hypothesis = 3

# the hypothesis refers to the driving time at certain speeds mentioned in the premise
if drive_time_at_50mph_hypothesis >= drive_time_at_50mph_premise:
    # check if the time driven at 50 mph in the hypothesis contradicts the premise
    label = "contradiction"
elif drive_time_at_60mph_hypothesis != drive_time_at_60mph_premise:
    # check if the time driven at 60 mph in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

