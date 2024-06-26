average_shirts_premise = 40
average_shirts_hypothesis = 60
shirts_purchased = 1

# the hypothesis talks about the average number of shirts each person now has, referenced also in the premise
if average_shirts_hypothesis <= (average_shirts_premise + shirts_purchased):
    # check if the hypothesis value contradicts the estimate of more than 'average_shirts_premise' plus 'shirts_purchased'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts
    # any average greater than 'average_shirts_premise' plus 'shirts_purchased' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
