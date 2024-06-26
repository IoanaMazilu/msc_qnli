house_cleaning_time_premise = 4
house_cleaning_time_hypothesis = 2

# The hypothesis refers to the time Bruce and Anne take to clean their house, which is also mentioned in the premise
if house_cleaning_time_premise < house_cleaning_time_hypothesis:
    # checking if the time taken to clean the house in the premise contradicts the estimate of more than 'house_cleaning_time_hypothesis' in the hypothesis
    label = "contradiction"
elif house_cleaning_time_premise == house_cleaning_time_hypothesis:
    # as the premise mentions a specific cleaning time, any other value would be a contradiction
    label = "contradiction"
else:
    # the premise value is consistent with the hypothesis statement that cleaning takes more than 'house_cleaning_time_hypothesis' hours
    # yet, the exact premise value cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)
