# Premise: Rose has 9.0 apples and 12.0 erasers, and she shares the apples among 3.0 friends.
# Hypothesis: Each friend got 3.0 apples.
# Golden Label: entailment

apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0
apples_per_friend_hypothesis = 3.0

# the hypothesis refers to the number of apples each friend got, which can be calculated from the premise
# compute the number of apples each friend got in the premise
apples_per_friend_premise = apples_premise / friends_premise
if apples_per_friend_hypothesis != apples_per_friend_premise:
    # check if the number of apples each friend got in the hypothesis contradicts the calculation from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

