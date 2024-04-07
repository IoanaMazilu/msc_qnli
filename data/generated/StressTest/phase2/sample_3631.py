# Premise: Faiza has more than 5 purses, she gives 3 purse as gift.
# Hypothesis: Faiza has 7 purses, she gives 3 purse as gift.
# Golden Label: neutral

purses_faiza_premise = 5
purses_faiza_hypothesis = 7
purses_gift_premise = 3
purses_gift_hypothesis = 3

# the hypothesis presents a number for Faiza's purses and the number of purses she gives as a gift, both referenced in the premise
if purses_faiza_hypothesis <= purses_faiza_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purses_faiza_premise'
    label = "contradiction"
elif purses_gift_hypothesis != purses_gift_premise:
    # check if the number of given purses in the hypothesis contradicts the number of given purses reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of Faiza's purses
    # any number of purses greater than 'purses_faiza_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

