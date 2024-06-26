average_shirts_premise = 40
average_shirts_hypothesis = 60
shirts_purchased = 2

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, mentioned also in the premise
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_shirts_premise'
    label = "contradiction"
else:
    # the number of purchased shirts does not affect the comparison between the premise and the hypothesis
    # any average number of shirts greater than 'average_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
