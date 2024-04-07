# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 2 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is more than 40, if all of them reached a shopping mall in Delhi and purchased 2 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

avg_shirts_premise = 60
avg_shirts_hypothesis = 40
shirts_bought = 2

# the hypothesis refers to the average number of shirts owned by the three individuals
if avg_shirts_premise <= avg_shirts_hypothesis:
    # check if the 'avg_shirts_hypothesis' contradicts the average number of shirts in the premise
    label = "contradiction"
else:
    # if the hypothesis value and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

