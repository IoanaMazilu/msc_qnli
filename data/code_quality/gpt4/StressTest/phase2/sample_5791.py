karen_speed_premise = 70
tom_speed_premise = 45
karen_speed_hypothesis = 60
tom_speed_hypothesis = 45

# the hypothesis talks about the speeds of Karen and Tom, referenced also in the premise
if karen_speed_hypothesis >= karen_speed_premise:
    # check if the speed of Karen in the hypothesis contradicts the estimate of less than 'karen_speed_premise'
    label = "contradiction"
elif tom_speed_hypothesis != tom_speed_premise:
    # check if the speed of Tom in the hypothesis contradicts the speed of Tom reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)