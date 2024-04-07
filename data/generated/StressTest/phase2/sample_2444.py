# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 54, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 34, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 54
average_shirts_hypothesis = 34
purchased_shirts = 8

# the hypothesis refers to the average number of shirts with each person, also mentioned in the premise
if average_shirts_hypothesis != average_shirts_premise:
    # check if the average number of shirts in the hypothesis contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

