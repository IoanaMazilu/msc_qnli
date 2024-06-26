average_speed_premise_to_beach = 40
average_speed_premise_home = 70
average_speed_hypothesis_to_beach = 80
average_speed_hypothesis_home = 70

# the hypothesis refers to the average speed of Carl's drive to the beach and back home, mentioned in the premise
if average_speed_hypothesis_to_beach <= average_speed_premise_to_beach:
    # check if the hypothesis value contradicts the estimate of more than 'average_speed_premise_to_beach'
    label = "contradiction"
elif average_speed_hypothesis_home!= average_speed_premise_home:
    # check if the average speed of Carl's drive home in the hypothesis contradicts the average speed of drive home reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed of Carl's drive to the beach
    # any average speed greater than 'average_speed_premise_to_beach' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
