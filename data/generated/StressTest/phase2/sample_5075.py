# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 5 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is less than 60, if all of them reached a shopping mall in Delhi and purchased 5 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 60
average_shirts_hypothesis = 60
additional_shirts = 5

# the hypothesis refers to the average number of shirts mentioned in the premise
if average_shirts_hypothesis + additional_shirts >= average_shirts_premise + additional_shirts:
    # check if the estimate of 'average_shirts_hypothesis' contradicts the number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

