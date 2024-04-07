# Premise: The average number of shirts with Salman, Ambani and Dalmiya is more than 10, if all of them reached a shopping mall in Delhi and purchased 5 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 5 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

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

