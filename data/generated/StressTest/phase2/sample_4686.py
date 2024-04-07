# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 72, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is less than 82, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

average_shirts_before_shopping_premise = 72
shirts_purchased_per_person = 12
average_shirts_after_shopping_premise = average_shirts_before_shopping_premise + shirts_purchased_per_person

average_shirts_after_shopping_hypothesis = 82

# the hypothesis refers to the average number of shirts after shopping for the same group of people mentioned in the premise
if average_shirts_after_shopping_premise >= average_shirts_after_shopping_hypothesis:
    # check if the calculated 'average_shirts_after_shopping_premise' contradicts the estimate of less than 'average_shirts_after_shopping_hypothesis'
    label = "contradiction"
else:
    # the hypothesis estimate for the average number of shirts after shopping does not contradict the premise, but it cannot be explicitly entailed from it
    label = "neutral"

print(label)

