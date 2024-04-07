# Premise: The average number of shirts with Salman, Ambani and Dalmiya is more than 39, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 69, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

shirt_average_premise = 39
shirt_average_hypothesis = 69
shirts_purchased = 12

# the hypothesis is about the average number of shirts with the three people, also mentioned in the premise
if shirt_average_hypothesis <= shirt_average_premise + shirts_purchased:
    # check if the hypothesis value contradicts the premise's estimate of more than 'shirt_average_premise' shirts each, after purchasing 'shirts_purchased'
    label = "contradiction"
elif shirt_average_hypothesis > shirt_average_premise + shirts_purchased:
    # the premise provides only an estimate of the average number of shirts each person has
    # any average number of shirts greater than 'shirt_average_premise' + 'shirts_purchased' is consistent with the premise, but cannot be explicitly entailed
    label = "neutral"
else:
    # if the number of shirts in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

