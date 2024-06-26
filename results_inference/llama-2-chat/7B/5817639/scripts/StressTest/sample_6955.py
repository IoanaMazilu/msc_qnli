average_shirts_premise = 80
average_shirts_hypothesis = 40

# the hypothesis talks about the average number of shirts held by Salman, Ambani, and Dalmiya
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts
    # any average number of shirts greater than 'average_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
