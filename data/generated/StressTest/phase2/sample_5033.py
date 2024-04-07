# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 1 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 80, if all of them reached a shopping mall in Delhi and purchased 1 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 60
shirts_purchased_each = 1
average_shirts_hypothesis = 80

# the hypothesis refers to the average number of shirts each person has after each of them purchased 1 shirt
new_average_shirts_premise = average_shirts_premise + shirts_purchased_each
if average_shirts_hypothesis == new_average_shirts_premise:
    # check if the new average number of shirts in the hypothesis matches the new average number of shirts in the premise (after purchasing)
    label = "entailment"
elif average_shirts_hypothesis != new_average_shirts_premise:
    # check if the new average number of shirts in the hypothesis contradicts the new average number of shirts in the premise (after purchasing)
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, and also cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

