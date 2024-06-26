average_shirts_premise = 80
average_shirts_hypothesis = 40
shirts_purchased = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya, also mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts
    # any average number of shirts less than 'average_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
