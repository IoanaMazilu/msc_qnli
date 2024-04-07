# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 6 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 70, if all of them reached a shopping mall in Delhi and purchased 6 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 60
average_shirts_hypothesis = 70
shirts_purchased = 6

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya after purchasing 6 shirts each
average_shirts_premise += shirts_purchased
average_shirts_hypothesis += shirts_purchased

if average_shirts_premise != average_shirts_hypothesis:
    # check if the average number of shirts in the hypothesis contradicts the average number of shirts in the premise after purchasing
    label = "contradiction"
else:
    # if the average number of shirts in the hypothesis does not contradict the average number of shirts in the premise after purchasing, we can infer entailment
    label = "entailment"

print(label)

