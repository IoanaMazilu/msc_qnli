total_purses_premise = 9
given_purses_premise = 3
total_purses_hypothesis = 4
given_purses_hypothesis = 3

# the hypothesis refers to the number of total purses and given purses mentioned in the premise
if given_purses_hypothesis != given_purses_premise:
    # check if the number of given purses in the hypothesis contradicts the number of given purses reported in the premise
    label = "contradiction"
elif total_purses_premise - given_purses_premise <= total_purses_hypothesis:
    # check if the remaining number of purses in the premise after giving away contradicts the estimate of more than 'total_purses_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
