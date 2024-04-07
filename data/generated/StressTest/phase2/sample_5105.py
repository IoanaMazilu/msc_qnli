# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 69, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is less than 69, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

average_shirts_premise = 69
average_shirts_hypothesis = 69
shirts_purchased = 12

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya and the number of shirts they purchased, also mentioned in the premise

# since they all purchased shirts, the new average number of shirts cannot be less than the initial average
if average_shirts_hypothesis < average_shirts_premise:
    # the hypothesis value contradicts the premise
    label = "contradiction"
elif average_shirts_hypothesis == average_shirts_premise:
    # if the hypothesis average is equal to the premise average, the hypothesis contradicts the premise because they all purchased additional shirts
    label = "contradiction"
else:
    # the premise gives only an average for the number of shirts and does not specify the total number of shirts each person has
    # the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

