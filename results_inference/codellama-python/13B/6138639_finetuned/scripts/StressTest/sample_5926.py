purses_faiza_premise = 34
purses_faiza_hypothesis = 14
gift_purses = 3

# the hypothesis talks about the number of purses Faiza has, referenced also in the premise
if purses_faiza_hypothesis >= purses_faiza_premise:
    # check if the hypothesis value contradicts the estimate of less than 'purses_faiza_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses
    # any number of purses less than 'purses_faiza_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
