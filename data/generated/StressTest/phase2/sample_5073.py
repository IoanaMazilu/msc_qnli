# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 5 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is more than 10, if all of them reached a shopping mall in Delhi and purchased 5 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

avg_shirts_premise = 60
avg_shirts_hypothesis = 10
shirts_purchased_each = 5

# the hypothesis refers to the average number of shirts with Salman, Ambani and Dalmiya mentioned in the premise
if avg_shirts_premise <= avg_shirts_hypothesis:
    # check if the estimate of 'avg_shirts_hypothesis' contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

