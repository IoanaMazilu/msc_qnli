hour_premise = 3
hour_hypothesis = 1
mph_premise = 50
mph_hypothesis = 60

# the hypothesis talks about the speed and duration of driving, referenced also in the premise
if hour_hypothesis <= hour_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hour_premise'
    label = "contradiction"
elif mph_hypothesis!= mph_premise:
    # check if the hypothesis speed contradicts the premise speed
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
