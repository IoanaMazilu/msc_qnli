house_cleaning_time_premise = 4
house_cleaning_time_hypothesis = 3

# the hypothesis refers to the time it takes to clean the house, which is also mentioned in the premise
if house_cleaning_time_hypothesis >= house_cleaning_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'house_cleaning_time_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, it is not contradictory but cannot be explicitly entailed
    label = "neutral"

print(label)
