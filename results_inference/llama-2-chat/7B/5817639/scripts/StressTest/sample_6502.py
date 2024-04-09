walking_rate_premise = 5
walking_rate_hypothesis = 3

# the hypothesis refers to the walking rate of Matthew and Johnny
if walking_rate_premise <= walking_rate_hypothesis:
    # check if the estimate of 'walking_rate_hypothesis' contradicts the number of km walked by Matthew in the premise
    label = "contradiction"
elif walking_rate_hypothesis - walking_rate_premise!= 1:
    # check if the number of km walked by Johnny in the hypothesis contradicts the number of km walked by Matthew in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
