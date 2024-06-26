purses_premise = 8
purses_hypothesis = 5
gift_premise = 3
gift_hypothesis = 3

# the hypothesis gives an estimate for the number of purses Faiza has
if purses_hypothesis >= purses_premise:
    # check if the estimate of 'purses_hypothesis' contradicts the number of purses reported in the premise
    label = "contradiction"
elif gift_hypothesis!= gift_premise:
    # check if the number of gifts in the hypothesis contradicts the number of gifts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
