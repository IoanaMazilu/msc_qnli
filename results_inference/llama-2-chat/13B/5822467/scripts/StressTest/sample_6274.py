jack_time_premise = 5
jack_time_hypothesis = 6
lee_time_premise = 10
lee_time_hypothesis = 10

# the hypothesis talks about the time taken by Jack and Lee to finish each lap
if jack_time_hypothesis <= jack_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jack_time_premise'
    label = "contradiction"
elif lee_time_hypothesis!= lee_time_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
