# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 40, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is less than 80, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

average_shirts_premise = 40
shirts_bought_each = 8
people_count = 3
average_shirts_hypothesis = 80

# Adding the bought shirts to the initial average to get the new average
new_average_shirts = average_shirts_premise + shirts_bought_each

# the hypothesis refers to the new average number of shirts with Salman, Ambani and Dalmiya
if new_average_shirts >= average_shirts_hypothesis:
    # check if the new average number of shirts contradicts the estimate of 'average_shirts_hypothesis'
    label = "contradiction"
elif new_average_shirts != average_shirts_hypothesis:
    # check if the new average number of shirts in the hypothesis contradicts the new average number of shirts
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

