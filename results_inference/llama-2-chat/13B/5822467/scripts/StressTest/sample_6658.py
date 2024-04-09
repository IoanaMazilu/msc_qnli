karen_speed_premise = 80
tom_speed_premise = 45
q_miles_premise = 0

karen_speed_hypothesis = 60
tom_speed_hypothesis = 45
q_miles_hypothesis = 0

# the hypothesis talks about the average speeds of Karen and Tom, and the number of Q miles driven
if karen_speed_hypothesis <= tom_speed_hypothesis:
    # check if the hypothesis value contradicts the estimate of Karen's speed being higher than Tom's
    label = "contradiction"
elif q_miles_hypothesis!= q_miles_premise:
    # check if the number of Q miles driven in the hypothesis contradicts the number of Q miles reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
