# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 40, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is less than 40, if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them then average number of shirt each of them now has.
# Golden Label: contradiction

avg_shirts_premise = 40
avg_shirts_hypothesis = 40
new_shirts_each = 8

# The hypothesis talks about the average number of shirts with Salman, Ambani, and Dalmiya, which is also referenced in the premise
# It also mentions that all of them purchased 8 new shirts each
new_avg_shirts_premise = avg_shirts_premise + new_shirts_each
new_avg_shirts_hypothesis = avg_shirts_hypothesis + new_shirts_each

if new_avg_shirts_hypothesis < avg_shirts_premise:
    # The hypothesis suggests that the average number of shirts is less than the initial number, which contradicts the premise
    label = "contradiction"
elif new_avg_shirts_hypothesis == new_avg_shirts_premise:
    # If the new average of shirts in the hypothesis matches the new average in the premise, we can infer entailment
    label = "entailment"
else:
    # Any other case would be neutral, as we cannot fully entail the hypothesis from the premise
    label = "neutral"

print(label)

