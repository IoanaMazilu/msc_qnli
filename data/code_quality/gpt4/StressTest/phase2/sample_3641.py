farm_building_time_premise = 6
farm_building_time_hypothesis = 6

# the hypothesis refers to the time James can make a new farm, mentioned in the premise
if farm_building_time_hypothesis >= farm_building_time_premise:
    # check if the hypothesis 'less than 6 years' contradicts the premise '6 years'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
