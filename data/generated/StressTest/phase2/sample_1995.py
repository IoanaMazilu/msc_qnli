# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 6 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is less than 70, if all of them reached a shopping mall in Delhi and purchased 6 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

average_shirts_premise = 60
purchased_shirts = 6
average_shirts_hypothesis = 70

# each person purchased additional shirts, which increases the average number of shirts they each have
average_shirts_premise += purchased_shirts

# the hypothesis refers to the average number of shirts each person has after purchasing more shirts
if average_shirts_premise >= average_shirts_hypothesis:
    # check if the hypothesis value contradicts the new average number of shirts
    label = "contradiction"
else:
    # the hypothesis gives an estimate for the new average number of shirts
    # the new average number of shirts being less than 'average_shirts_hypothesis' can be inferred from the premise, hence we have entailment
    label = "entailment"

print(label)

