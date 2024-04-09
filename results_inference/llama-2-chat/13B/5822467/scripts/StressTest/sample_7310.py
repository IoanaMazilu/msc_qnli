minutes_premise = 4
words_premise = 8
rate_premise = 4

# the hypothesis talks about typing at a rate and the number of words to be typed, both referenced also in the premise
if words_hypothesis <= words_premise:
    # check if the hypothesis value contradicts the estimate of 'words_premise'
    label = "contradiction"
elif minutes_hypothesis!= minutes_premise:
    # check if the number of minutes in the hypothesis contradicts the number of minutes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of words to be typed
    # any number of words less than 'words_premise' typed in less than'minutes_premise' minutes is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
