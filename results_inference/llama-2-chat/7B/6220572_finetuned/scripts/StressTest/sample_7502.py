pat_speed_premise = 9
pat_speed_hypothesis = 9
cara_speed_premise = 5
cara_speed_hypothesis = 5

# the hypothesis talks about the running speed of Pat and Cara, referenced also in the premise
if pat_speed_hypothesis <= pat_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pat_speed_premise'
    label = "contradiction"
elif cara_speed_hypothesis!= cara_speed_premise:
    # check if the number of sold pies in the hypothesis contradicts the number of sold pies reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
