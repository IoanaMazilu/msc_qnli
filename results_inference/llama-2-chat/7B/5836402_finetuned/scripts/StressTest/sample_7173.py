purses_faiza_premise = 8
given_purses_premise = 3
purses_faiza_hypothesis = 5
given_purses_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and the number of purses she gives as a gift
if purses_faiza_premise <= purses_faiza_hypothesis:
    # check if the estimate of 'purses_faiza_hypothesis' contradicts the number of purses Faiza has in the premise
    label = "contradiction"
elif given_purses_hypothesis!= given_purses_premise:
    # check if the number of purses Faiza gives as a gift in the hypothesis contradicts the number of purses given in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
