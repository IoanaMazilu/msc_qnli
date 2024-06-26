purses_faiza_premise = 14
purses_faiza_hypothesis = 34
purses_gift_premise = 3
purses_gift_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and gives as a gift, mentioned in the premise
if purses_faiza_premise!= purses_faiza_hypothesis:
    # check if the number of purses Faiza has in the hypothesis contradicts the number of purses reported in the premise
    label = "contradiction"
elif purses_gift_premise!= purses_gift_hypothesis:
    # check if the number of purses Faiza gives as a gift in the hypothesis contradicts the number of purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)