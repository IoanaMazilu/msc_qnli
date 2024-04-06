# Premise: Jesse has 21.0 bananas, and he shares them among 3.0 friends.
# Hypothesis: Each friend gets 7.0 bananas.
# Golden Label: entailment

bananas_premise = 21.0
friends_premise = 3.0
bananas_per_friend_hypothesis = 7.0

# the hypothesis refers to the number of bananas each friend gets, which can be calculated from the premise
# compute the number of bananas each friend gets in the premise
bananas_per_friend_premise = bananas_premise / friends_premise

if bananas_per_friend_hypothesis != bananas_per_friend_premise:
    # check if the number of bananas per friend in the hypothesis contradicts the calculated number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

