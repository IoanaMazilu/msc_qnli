purses_faiza_premise = 8
purses_faiza_hypothesis = 5
gifts_faiza_premise = 3
gifts_faiza_hypothesis = 3

# the hypothesis talks about the number of purses in Faiza's possession
# the premise gives an estimate for the number of purses in Faiza's possession
if purses_faiza_hypothesis <= purses_faiza_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purses_faiza_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses
    # any number of purses greater than 'purses_faiza_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
