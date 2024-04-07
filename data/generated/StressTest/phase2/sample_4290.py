# Premise: Bob had x number of sweets and wanted to share it with his 6 friends.
# Hypothesis: Bob had x number of sweets and wanted to share it with his less than 7 friends.
# Golden Label: entailment

friends_premise = 6
friends_hypothesis = 7

# the hypothesis talks about the number of friends Bob wanted to share his sweets with, same as the premise
if friends_premise >= friends_hypothesis:
    # check if the number of friends in the premise contradicts the estimate of less than 'friends_hypothesis'
    label = "contradiction"
else:
    # The hypothesis value does not contradict the premise but also cannot be explicitly entailed from the premise since 'less than 7' includes 6 but also all the numbers below 6
    label = "neutral"

print(label)

