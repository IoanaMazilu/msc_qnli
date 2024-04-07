# Premise: The average number of shirts with Salman, Ambani and Dalmiya is more than 24, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 54, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

avg_shirts_premise = 24
avg_shirts_hypothesis = 54
additional_shirts_each = 8

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya, both before and after purchasing some more shirts
if avg_shirts_hypothesis <= avg_shirts_premise + additional_shirts_each:
    # check if the hypothesis value contradicts the estimate of more than 'avg_shirts_premise' plus the additional shirts each of them has bought
    label = "contradiction"
else:
    # the premise gives only an estimate for the average number of shirts
    # any average number of shirts greater than 'avg_shirts_premise' plus the additional shirts is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

