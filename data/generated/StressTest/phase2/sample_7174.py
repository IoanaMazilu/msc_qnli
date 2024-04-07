# Premise: Faiza has more than 5 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has 8 purses, she gives 3 purse as gift.
# Golden Label: neutral

purses_faiza_premise = 5
purses_faiza_hypothesis = 8
purses_gift_premise = 3
purses_gift_hypothesis = 3

# the hypothesis talks about the number of purses Faiza has and the number of purses she gives as a gift, which are both referenced in the premise
if purses_faiza_hypothesis <= purses_faiza_premise:
    # check if the number of purses in the hypothesis contradicts the estimate of more than 'purses_faiza_premise'
    label = "contradiction"
elif purses_gift_hypothesis != purses_gift_premise:
    # check if the number of gifted purses in the hypothesis contradicts the number of gifted purses reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses
    # 'purses_faiza_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

