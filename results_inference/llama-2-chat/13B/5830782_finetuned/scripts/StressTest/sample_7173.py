purses_faiza_premise = 8
purses_given_premise = 3
purses_faiza_hypothesis = 5
purses_given_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and gives as a gift, mentioned in the premise
if purses_faiza_premise <= purses_faiza_hypothesis:
    # check if the estimate of 'purses_faiza_hypothesis' contradicts the number of purses Faiza has in the premise
    label = "contradiction"
elif purses_given_premise!= purses_given_hypothesis:
    # check if the number of purses given as a gift in the hypothesis contradicts the number of purses given as a gift reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
