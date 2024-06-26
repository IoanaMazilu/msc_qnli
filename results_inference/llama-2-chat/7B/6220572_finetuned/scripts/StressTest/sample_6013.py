average_speed_karen_premise = 20
average_speed_karen_hypothesis = 60
average_speed_tom_premise = 45
average_speed_tom_hypothesis = 45

# the hypothesis refers to the average speed of Karen and Tom mentioned in the premise
if average_speed_karen_hypothesis <= average_speed_karen_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_speed_karen_premise'
    label = "contradiction"
elif average_speed_tom_hypothesis!= average_speed_tom_premise:
    # check if the number of driven miles in the hypothesis contradicts the number of driven miles reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of driven miles
    # any number of driven miles consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
