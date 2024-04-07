# Premise: Bob had x number of sweets and wanted to share it with his 6 friends.
# Hypothesis: Bob had x number of sweets and wanted to share it with his 1 friends.
# Golden Label: contradiction

friends_premise = 6
friends_hypothesis = 1

# the hypothesis talks about the number of friends Bob wants to share his sweets with, referenced also in the premise
if friends_hypothesis != friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends in the premise
    label = "contradiction"
else:
    # it's unlikely this else branch would be reached because friends_hypothesis was explicitly set to a different value than friends_premise
    label = "entailment"

print(label)

