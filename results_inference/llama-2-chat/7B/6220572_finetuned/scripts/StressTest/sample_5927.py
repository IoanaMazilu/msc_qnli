purses_premise = 14
purses_hypothesis = 34
given_purses_premise = 3
given_purses_hypothesis = 3

# the hypothesis refers to the number of purses and the number of given purses mentioned in the premise
if purses_hypothesis <= purses_premise:
    # check if the estimate of 'purses_hypothesis' contradicts the number of purses in the premise
    label = "contradiction"
elif given_purses_hypothesis!= given_purses_premise:
    # check if the number of given purses in the hypothesis contradicts the number of given purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
