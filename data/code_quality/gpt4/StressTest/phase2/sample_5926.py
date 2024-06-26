purses_premise = 34
purses_hypothesis = 14
gift_purses = 3

# the hypothesis talks about the number of purses Faiza has and the number of purses she gives as gifts, both mentioned in the premise
if purses_hypothesis >= purses_premise:
    # check if the number of purses in the hypothesis contradicts the estimate of less than 'purses_premise'
    label = "contradiction"
elif gift_purses != 3:
    # check if the number of gift purses in the hypothesis contradicts the number of gift purses reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses Faiza has
    # any number of purses less than 'purses_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
