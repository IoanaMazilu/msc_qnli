average_speed_home_premise = 40
average_speed_beach_premise = 70
average_speed_home_hypothesis = 80
average_speed_beach_hypothesis = 70

# the hypothesis refers to the average speeds Carl drove at, mentioned also in the premise
if average_speed_home_hypothesis <= average_speed_home_premise:
    # check if the average speed home in the hypothesis contradicts the premise
    label = "contradiction"
elif average_speed_beach_hypothesis!= average_speed_beach_premise:
    # check if the average speed to the beach in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only a lower limit for the average speed home
    # any speed greater than 'average_speed_home_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
