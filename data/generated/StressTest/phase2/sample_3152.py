# Premise: City A to city B, Ameer drove for 1 hour at 60 mph and for 3 hours at 50 mph.
# Hypothesis: City A to city B, Ameer drove for 3 hour at 60 mph and for 3 hours at 50 mph.
# Golden Label: contradiction

drive_time_at_60mph_premise = 1
drive_time_at_60mph_hypothesis = 3
drive_time_at_50mph_premise = 3
drive_time_at_50mph_hypothesis = 3

# the hypothesis provides information about the driving time at certain speeds
# that Ameer drove from city A to city B, which is also reported in the premise
if drive_time_at_60mph_hypothesis != drive_time_at_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at the same speed reported in the premise
    label = "contradiction"
elif drive_time_at_50mph_hypothesis != drive_time_at_50mph_premise:
    # check if the driving time at 50 mph in the hypothesis contradicts the driving time at the same speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

