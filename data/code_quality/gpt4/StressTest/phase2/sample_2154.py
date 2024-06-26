pat_stretch_time_premise = 15
pat_stretch_time_hypothesis = 75

# The hypothesis refers to the time Pat takes to stretch, which is also mentioned in the premise
if pat_stretch_time_premise >= pat_stretch_time_hypothesis:
    # Check if the actual time Pat takes to stretch contradicts the estimate of less than 'pat_stretch_time_hypothesis'
    label = "contradiction"
elif pat_stretch_time_premise < pat_stretch_time_hypothesis:
    # The premise gives an exact time for Pat's stretching. 
    # Any stretching time less than 'pat_stretch_time_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
