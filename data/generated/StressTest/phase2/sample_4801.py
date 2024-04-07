# Premise: The average number of shirts with Salman, Ambani and Dalmiya is more than 40, if all of them reached a shopping mall in Delhi and purchased 2 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 2 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

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

