# Premise: The average number of shirts with Salman, Ambani and Dalmiya is more than 40, if all of them reached a shopping mall in Delhi and purchased 1 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 1 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

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

