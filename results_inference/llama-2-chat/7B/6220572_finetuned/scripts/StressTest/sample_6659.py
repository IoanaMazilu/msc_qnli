karen_speed_premise = 60
karen_speed_hypothesis = 70
tom_speed_premise = 45
tom_speed_hypothesis = 45
q_miles_premise = 0
q_miles_hypothesis = 0

# the hypothesis talks about the average speed of Karen and Tom, referenced also in the premise
if karen_speed_hypothesis!= karen_speed_premise:
    # check if the estimate of 'karen_speed_hypothesis' contradicts the average speed of Karen in the premise
    label = "contradiction"
elif tom_speed_hypothesis!= tom_speed_premise:
    # check if the average speed of Tom in the hypothesis contradicts the average speed of Tom reported in the premise
    label = "contradiction"
elif q_miles_hypothesis!= q_miles_premise:
    # check if the number of Q miles in the hypothesis contradicts the number of Q miles reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
