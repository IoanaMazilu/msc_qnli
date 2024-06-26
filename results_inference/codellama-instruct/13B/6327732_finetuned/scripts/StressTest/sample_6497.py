premise_distance = 140 # km
premise_time = 44 # min
premise_speed = 50 # km/hr

hypothesis_distance = 140 # km
hypothesis_time = 14 # min
hypothesis_speed = 50 # km/hr

# the hypothesis refers to the distance and time mentioned in the premise
if hypothesis_distance!= premise_distance:
    # check if the hypothesis value contradicts the distance in the premise
    label = "contradiction"
elif hypothesis_time!= premise_time:
    # check if the hypothesis value contradicts the time in the premise
    label = "contradiction"
elif hypothesis_speed!= premise_speed:
    # check if the hypothesis value contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
