# Premise: The average number of shirts with Salman, Ambani and Dalmiya is less than 82, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 72, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

average_shirts_premise = 82
average_shirts_hypothesis = 72
shirts_purchased = 12

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya,
# also referenced in the premise, and the number of shirts they purchased

if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis value contradicts the estimate of less than 'average_shirts_premise'
    label = "contradiction"
elif average_shirts_hypothesis + shirts_purchased != average_shirts_premise + shirts_purchased:
    # check if the hypothesis value plus the number of shirts purchased contradicts the premise value plus the number of shirts purchased
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts
    # any number of shirts less than 'average_shirts_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

