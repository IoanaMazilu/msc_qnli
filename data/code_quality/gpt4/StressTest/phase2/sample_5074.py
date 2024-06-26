average_shirts_premise = 10
average_shirts_hypothesis = 60
shirts_purchased = 5

# the hypothesis talks about the average number of shirts after each of them purchased a certain number of shirts
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of more than 'average_shirts_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts
    # any average number of shirts greater than 'average_shirts_premise' + 'shirts_purchased' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
