# Premise: city A to city B, Andrew drove for less than 2 hour at 50 mph and for 3 hours at 60 mph.
# Hypothesis: city A to city B, Andrew drove for 1 hour at 50 mph and for 3 hours at 60 mph.
# Golden Label: neutral

drive_time_50mph_premise = 2  # hours
drive_time_50mph_hypothesis = 1  # hours
drive_time_60mph_premise = 3  # hours
drive_time_60mph_hypothesis = 3  # hours

# the hypothesis refers to the time Andrew drove at certain speeds from city A to city B, mentioned in the premise
if drive_time_50mph_hypothesis >= drive_time_50mph_premise:
    # check if the time driven at 50 mph in the hypothesis contradicts the premise's 'less than 2 hours' estimate
    label = "contradiction"
elif drive_time_60mph_hypothesis != drive_time_60mph_premise:
    # check if the time driven at 60 mph in the hypothesis contradicts the time driven at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

