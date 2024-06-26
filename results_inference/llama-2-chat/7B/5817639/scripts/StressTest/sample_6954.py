average_shirts_premise = 40
average_shirts_hypothesis = 80

# the hypothesis talks about the number of shirts each person has after purchasing 8 shirts each, referenced also in the premise
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of 'average_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts greater than 'average_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
