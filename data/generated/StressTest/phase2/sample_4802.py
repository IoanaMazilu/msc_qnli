# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 2 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 70, if all of them reached a shopping mall in Delhi and purchased 2 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 60
average_shirts_hypothesis = 70
shirts_purchased_each = 2

# the hypothesis refers to the average number of shirts each person has, as mentioned in the premise
if average_shirts_premise + shirts_purchased_each != average_shirts_hypothesis:
    # check if the hypothesis value contradicts the premise value plus the number of shirts each person purchased
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

