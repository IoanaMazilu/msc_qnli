purses_faiza_premise = 8
purses_given_premise = 3
purses_faiza_hypothesis = 5
purses_given_hypothesis = 3

# the hypothesis refers to the number of Faiza's purses and the number of purses given as gifts, mentioned in the premise
if purses_faiza_premise <= purses_faiza_hypothesis:
    # check if the estimate of 'purses_faiza_hypothesis' contradicts the number of purses Faiza has in the premise
    label = "contradiction"
elif purses_given_hypothesis!= purses_given_premise:
    # check if the number of given purses in the hypothesis contradicts the number of given purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
