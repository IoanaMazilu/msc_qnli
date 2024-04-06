# Premise: Rose has 9.0 apples and 12.0 erasers, and she shares the apples among 3.0 friends.
# Hypothesis: Each friend got 7.0 apples.
# Golden Label: contradiction

apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0
apples_per_friend_hypothesis = 7.0

# the hypothesis refers to the number of apples each friend got, which can be infered from the premise
# calculate the number of apples each friend got from the premise
apples_per_friend_premise = apples_premise / friends_premise
if apples_per_friend_hypothesis != apples_per_friend_premise:
    # check if the number of apples each friend got in the hypothesis contradicts the number of apples each friend got from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

