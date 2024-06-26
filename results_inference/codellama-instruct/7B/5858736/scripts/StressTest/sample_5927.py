# the hypothesis refers to the number of purses and the number of purses given as a gift
if purses_faiza_hypothesis <= purses_faiza_premise:
    # check if the estimate of 'purses_faiza_hypothesis' contradicts the number of purses in the premise
    label = "contradiction"
elif gifts_faiza_hypothesis!= gifts_faiza_premise:
    # check if the number of gifts given by Faiza in the hypothesis contradicts the number of gifts mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
