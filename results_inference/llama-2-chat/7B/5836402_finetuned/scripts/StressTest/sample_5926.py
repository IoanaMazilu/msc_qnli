purses_faiza_premise = 34
given_purses_premise = 3
purses_Faiza_hypothesis = 14
given_purses_hypothesis = 3

# the hypothesis talks about the number of purses Faiza has and the number of purses she gave as gift, referenced also in the premise
if purses_Faiza_hypothesis <= purses_faiza_premise:
    # check if the hypothesis value contradicts the estimate of more than 'purses_faiza_premise'
    label = "contradiction"
elif given_purses_hypothesis!= given_purses_premise:
    # check if the number of purses Faiza gave as gift in the hypothesis contradicts the number of purses she gave as gift reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of purses Faiza has
    # any number of purses less than 'purses_faiza_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
