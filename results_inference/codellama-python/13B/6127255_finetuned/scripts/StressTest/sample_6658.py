karen_speed_premise = 80
karen_speed_hypothesis = 60
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis talks about the average speeds of Karen and Tom, referenced also in the premise
if karen_speed_hypothesis >= karen_speed_premise:
    # check if the hypothesis value contradicts the estimate of less than 'karen_speed_premise'
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the average speed of Tom in the hypothesis contradicts the average speed of Tom reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the average speed of Karen
    # any average speed of Karen less than 'karen_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)