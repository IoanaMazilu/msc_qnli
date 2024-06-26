purses_faiza_premise = 8
purses_faiza_hypothesis = 4
purses_gift_premise = 3
purses_gift_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and gives as gifts, mentioned in the premise
if purses_faiza_premise!= purses_faiza_hypothesis:
    # check if the number of purses Faiza has in the hypothesis contradicts the number of purses she has in the premise
    label = "contradiction"
elif purses_gift_hypothesis!= purses_gift_premise:
    # check if the number of purses given as gifts in the hypothesis contradicts the number of purses given as gifts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
