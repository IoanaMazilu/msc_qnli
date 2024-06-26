average_speed_to_beach_premise = 40
average_speed_to_beach_hypothesis = 80
average_speed_home_premise = 70
average_speed_home_hypothesis = 70

# the hypothesis refers to the average speeds of Carl's drive to the beach and back home, mentioned in the premise
if average_speed_to_beach_hypothesis <= average_speed_to_beach_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_speed_to_beach_premise'
    label = "contradiction"
elif average_speed_home_hypothesis!= average_speed_home_premise:
    # check if the average speed home in the hypothesis contradicts the average speed home reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed to the beach
    # any average speed greater than 'average_speed_to_beach_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
