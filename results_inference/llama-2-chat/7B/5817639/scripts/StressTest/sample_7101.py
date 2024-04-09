miles_driven_premise = 240
miles_driven_hypothesis = 340
speed_premise = 60
speed_hypothesis = 40

# the hypothesis talks about the total distance driven and the speed at which it was driven
if miles_driven_hypothesis <= miles_driven_premise:
    # check if the hypothesis value contradicts the estimate of total distance driven in the premise
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the hypothesis speed contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
