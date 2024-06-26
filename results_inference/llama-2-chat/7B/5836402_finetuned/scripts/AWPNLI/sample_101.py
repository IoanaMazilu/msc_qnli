bananas_total_premise = 21.0
friends_premise = 3.0
bananas_per_friend_hypothesis = 2.0

# the hypothesis refers to the number of bananas per friend, which is also mentioned in the premise
# compute the number of bananas each friend gets from the premise
bananas_per_friend_premise = bananas_total_premise / friends_premise
if bananas_per_friend_hypothesis!= bananas_per_friend_premise:
    # check if the number of bananas per friend from the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
