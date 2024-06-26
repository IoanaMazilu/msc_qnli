apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0
apples_hypothesis = 3.0

# the hypothesis refers to the number of apples each friend got, which is also mentioned in the premise
# compute the total number of apples each friend got in the premise
apples_each_friend_premise = apples_premise / friends_premise

if apples_hypothesis!= apples_each_friend_premise:
    # check if the number of apples each friend got in the hypothesis contradicts the number of apples each friend got in the premise
    label = "contradiction"
else:
    label = "entailment"

print(label)
