# Premise: City A to city B, Andrew drove for less than 2 hr at 44 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for 1 hr at 44 mph and for 3 hours at 60 mph.
# Golden Label: neutral

# Define the variables for the premise and hypothesis
drive_time_less_than_premise = 2
drive_time_hypothesis = 1
drive_time_at_60mph_premise = 3
drive_time_at_60mph_hypothesis = 3

# The hypothesis refers to the drive times mentioned in the premise
if drive_time_hypothesis > drive_time_less_than_premise:
    # Check if the drive time in the hypothesis contradicts the estimate of less than 'drive_time_less_than_premise' in the premise
    label = "contradiction"
elif drive_time_at_60mph_hypothesis != drive_time_at_60mph_premise:
    # Check if the drive time at 60 mph in the hypothesis contradicts the drive time at 60 mph in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

