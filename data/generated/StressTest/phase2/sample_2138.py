# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 3 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 70, if all of them reached a shopping mall in Delhi and purchased 3 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 60
average_shirts_hypothesis = 70
shirts_purchased_each = 3

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya after each of them purchased 3 more shirts
if average_shirts_hypothesis != average_shirts_premise + shirts_purchased_each:
    # check if the hypothesis value contradicts the premise value increased with the number of shirts purchased by each person
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value increased with the number of shirts purchased by each person, we can infer entailment
    label = "entailment"

print(label)

