purses_faiza_premise = 34
purses_faiza_hypothesis = 14
purses_gift_premise = 3
purses_gift_hypothesis = 3

# the hypothesis refers to the number of Faiza's purses and the number of purses she gives as gifts, mentioned in the premise
if purses_faiza_hypothesis >= purses_faiza_premise:
    # check if the number of purses in the hypothesis contradicts the estimate of less than 'purses_faiza_premise'
    label = "contradiction"
elif purses_gift_hypothesis!= purses_gift_premise:
    # check if the number of gift purses in the hypothesis contradicts the number of gift purses reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses Faiza has
    # any number of purses less than 'purses_faiza_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
