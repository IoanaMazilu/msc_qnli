speed_premise = 1
speed_hypothesis = 9

# the hypothesis talks about the speed of Sacha and Bruno, which are also mentioned in the premise
if speed_hypothesis <= speed_premise:
    # check if the hypothesis value contradicts the estimate of Sacha's speed in the premise
    label = "contradiction"
elif speed_hypothesis - speed_premise!= 4:
    # check if the difference between the hypothesis and premise speeds contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
