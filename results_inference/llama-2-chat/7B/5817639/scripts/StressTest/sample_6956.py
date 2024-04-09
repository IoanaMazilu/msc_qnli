average_shirts_premise = 40
average_shirts_hypothesis = 30

# the hypothesis talks about the number of shirts each of Salman, Ambani and Dalmiya have after purchasing 8 shirts each in Delhi
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of 'average_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts, and the hypothesis value is consistent with it
    label = "neutral"

print(label)
