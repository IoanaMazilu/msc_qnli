# Premise: The average number of shirts with Salman, Ambani and Dalmiya is less than 80, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 40, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

average_shirts_premise = 80
average_shirts_hypothesis = 40
shirts_purchased_each = 8

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if average_shirts_hypothesis >= average_shirts_premise:
    # check if the estimate of 'average_shirts_hypothesis' contradicts the number of average shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

