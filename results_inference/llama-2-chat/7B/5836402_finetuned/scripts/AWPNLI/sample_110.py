apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0
apples_hypothesis = 3.0

# the hypothesis refers to the number of apples each friend got, which is also mentioned in the premise
# compute the total number of apples each friend got from the premise
apples_each_friend_premise = apples_premise / friends_premise
if apples_each_friend_hypothesis!= apples_each_friend_premise:
    # check if the number of apples each friend got from the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
