# Premise: Faiza has more than 4 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has 9 purses, she gives 3 purse as gift.
# Golden Label: neutral

purses_faiza_premise = 4
purses_faiza_hypothesis = 9
purses_gift_premise = 3
purses_gift_hypothesis = 3

# the hypothesis talks about the number of purses Faiza has and gives as gift, referenced also in the premise
if purses_faiza_hypothesis <= purses_faiza_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purses_faiza_premise'
    label = "contradiction"
elif purses_gift_hypothesis != purses_gift_premise:
    # check if the number of gift purses in the hypothesis contradicts the number of gift purses reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses
    # any number of purses greater than 'purses_faiza_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

