# Premise: Faiza has 8 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has 4 purses, she gives 3 purse as gift.
# Golden Label: contradiction

purses_faiza_premise = 8
gift_purses_premise = 3
purses_faiza_hypothesis = 4
gift_purses_hypothesis = 3

# the hypothesis refers to the number of purses Faiza has and the number of purses she gives as a gift
if purses_faiza_premise - gift_purses_premise != purses_faiza_hypothesis:
    # check if the remaining number of purses in the hypothesis contradicts the remaining number of purses in the premise after gifting
    label = "contradiction"
elif gift_purses_hypothesis != gift_purses_premise:
    # check if the number of gifted purses in the hypothesis contradicts the number of gifted purses reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

