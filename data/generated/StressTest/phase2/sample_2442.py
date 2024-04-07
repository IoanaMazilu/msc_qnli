# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 54, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is more than 24, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

average_shirts_premise = 54
average_shirts_hypothesis = 24
shirts_purchased_each = 8

# add the new purchased shirts to the average number of shirts each person has according to the premise
average_shirts_premise += shirts_purchased_each

# the hypothesis talks about the average number of shirts each person has, referenced also in the premise
if average_shirts_premise <= average_shirts_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'average_shirts_hypothesis'
    label = "contradiction"
elif average_shirts_hypothesis > average_shirts_premise:
    # check if the hypothesis value contradicts the total number of shirts each person has according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

