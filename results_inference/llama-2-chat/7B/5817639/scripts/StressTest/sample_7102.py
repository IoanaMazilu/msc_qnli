miles_premise = 340
miles_hypothesis = 240
speed_premise = 60
speed_hypothesis = 40

# the hypothesis talks about the distance and speed of Joe's journey, referenced also in the premise
if miles_hypothesis <= miles_premise:
    # check if the hypothesis value contradicts the estimate of'miles_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
