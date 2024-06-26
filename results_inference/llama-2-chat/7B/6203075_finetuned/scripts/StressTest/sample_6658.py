karen_speed_premise = 80
karen_speed_hypothesis = 60
tom_speed_premise = 45
tom_speed_hypothesis = 45

# the hypothesis talks about the speed of Karen and Tom, which are also mentioned in the premise
if karen_speed_hypothesis >= karen_speed_premise:
    # check if the hypothesis value contradicts the premise of Karen's speed being less than 'karen_speed_premise'
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the speed of Tom in the hypothesis contradicts the speed of Tom in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of miles Tom will drive
    # any number of miles less than 'karen_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
