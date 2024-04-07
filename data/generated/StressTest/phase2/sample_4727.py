# Premise: City A to city B, Andrew drove for 1 hr at 48 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for 4 hr at 48 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

# define the variables
drive_time_at_48mph_premise = 1
drive_time_at_48mph_hypothesis = 4
drive_time_at_60mph_premise = 3
drive_time_at_60mph_hypothesis = 3

# the hypothesis refers to the driving time at two different speeds mentioned in the premise
if drive_time_at_48mph_premise != drive_time_at_48mph_hypothesis:
    # check if the driving time at 48mph in the hypothesis contradicts the driving time at 48mph reported in the premise
    label = "contradiction"
elif drive_time_at_60mph_premise != drive_time_at_60mph_hypothesis:
    # check if the driving time at 60mph in the hypothesis contradicts the driving time at 60mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

