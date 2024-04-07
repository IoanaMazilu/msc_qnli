# Premise: City A to city B, Andrew drove for 1 hour at 50 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Andrew drove for less than 1 hour at 50 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

# Variables for the driving time in hours at 50 mph
driving_time_50mph_premise = 1
driving_time_50mph_hypothesis = 1

# Variables for the driving time in hours at 60 mph
driving_time_60mph_premise = 3
driving_time_60mph_hypothesis = 3

# The hypothesis refers to the driving time at two specific speeds mentioned in the premise
if driving_time_50mph_hypothesis >= driving_time_50mph_premise:
    # check if the driving time at 50 mph in the hypothesis contradicts the driving time at 50 mph mentioned in the premise
    label = "contradiction"
elif driving_time_60mph_hypothesis != driving_time_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph mentioned in the premise
    label = "contradiction"
else:
    # if the driving times in the hypothesis do not contradict the driving times in the premise
    label = "neutral"

print(label)

