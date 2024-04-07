# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 4 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is less than 60, if all of them reached a shopping mall in Delhi and purchased 4 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 60
purchased_shirts = 4
average_shirts_hypothesis = 60

# the hypothesis refers to the average number of shirts owned by the three individuals, which is also referred to in the premise
if average_shirts_hypothesis + purchased_shirts <= average_shirts_premise:
    # check if the average number of shirts in the hypothesis contradicts the average number of shirts mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

