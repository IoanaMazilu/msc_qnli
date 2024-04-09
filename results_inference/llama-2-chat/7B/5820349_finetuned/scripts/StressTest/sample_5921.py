average_speed_premise_to_beach = 80
average_speed_premise_from_beach = 70
average_speed_hypothesis_to_beach = 80
average_speed_hypothesis_from_beach = 70

# the hypothesis refers to the average speed of Carl's drives to and from the beach, mentioned in the premise
if average_speed_hypothesis_to_beach <= average_speed_premise_to_beach:
    # check if the hypothesis value contradicts the premise value for the speed to the beach
    label = "contradiction"
elif average_speed_hypothesis_from_beach!= average_speed_premise_from_beach:
    # check if the hypothesis value contradicts the premise value for the speed from the beach
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed to the beach
    # any speed greater than 'average_speed_premise_to_beach' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
