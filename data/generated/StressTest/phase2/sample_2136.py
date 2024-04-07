# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 3 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is more than 30, if all of them reached a shopping mall in Delhi and purchased 3 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

avg_shirts_premise = 60
avg_shirts_hypothesis = 30
shirts_bought_each = 3

# the hypothesis talks about the average number of shirts with Salman, Ambani, and Dalmiya, also mentioned in the premise
# both premise and hypothesis also mention that each of them bought 3 shirts at a shopping mall in Delhi
if avg_shirts_premise <= avg_shirts_hypothesis:
    # check if the estimate of 'avg_shirts_hypothesis' contradicts the average number of shirts in the premise
    label = "contradiction"
elif avg_shirts_premise + shirts_bought_each <= avg_shirts_hypothesis + shirts_bought_each:
    # check if the new average number of shirts each of them has contradicts the number in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

