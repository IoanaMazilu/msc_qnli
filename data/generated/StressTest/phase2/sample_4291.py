# Premise: Bob had x number of sweets and wanted to share it with his less than 7 friends.
# Hypothesis: Bob had x number of sweets and wanted to share it with his 6 friends.
# Golden Label: neutral

friends_premise = 7
friends_hypothesis = 6

# the hypothesis talks about the number of friends with whom Bob wants to share his sweets
if friends_hypothesis >= friends_premise:
    # check if the number of friends in the hypothesis contradicts the premise's estimate of less than 'friends_premise'
    label = "contradiction"
elif friends_hypothesis < friends_premise:
    # if the number of friends in the hypothesis is less than 'friends_premise' then it can be entailed from the premise
    label = "entailment"

print(label)

