driven_time_premise = 3
driven_time_hypothesis = 1
speed_premise = 42
speed_hypothesis = 60

# the hypothesis talks about the speed and duration of driving, referenced also in the premise
if driven_time_hypothesis <= driven_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'driven_time_premise'
    label = "contradiction"
elif speed_hypothesis!= speed_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
