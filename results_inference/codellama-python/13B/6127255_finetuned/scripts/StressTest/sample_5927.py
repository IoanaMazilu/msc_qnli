purses_faiza_premise = 14
purses_faiza_hypothesis = 34
purses_gift_premise = 3
purses_gift_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and the number of purses she gives as gifts, both mentioned in the premise
if purses_faiza_hypothesis!= purses_faiza_premise:
    # check if the number of purses in the hypothesis contradicts the number of purses reported in the premise
    label = "contradiction"
elif purses_gift_hypothesis!= purses_gift_premise:
    # check if the number of gift purses in the hypothesis contradicts the number of gift purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)