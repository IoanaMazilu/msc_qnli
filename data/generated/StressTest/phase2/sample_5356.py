# Premise: The average number of shirts with Salman, Ambani and Dalmiya is more than 20, if all of them reached a shopping mall in Delhi and purchased 4 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 4 shirts each of them then average number of shirt each of them now has.
# Golden Label: neutral

average_shirts_premise = 20
average_shirts_hypothesis = 60
shirts_purchased_each = 4

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if average_shirts_hypothesis <= average_shirts_premise:
    # check if the 'average_shirts_hypothesis' contradicts the premise of more than 'average_shirts_premise'
    label = "contradiction"
elif average_shirts_premise + shirts_purchased_each != average_shirts_hypothesis:
    # check if the average number of shirts after purchase in the hypothesis contradicts the calculated average after purchase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and calculations do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

