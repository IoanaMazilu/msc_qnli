bananas_premise = 21.0
friends_premise = 3.0
bananas_per_friend_hypothesis = 2.0

# the hypothesis refers to the number of bananas each friend gets, which is also mentioned in the premise
# compute the total number of bananas in the premise
total_bananas_premise = bananas_premise * friends_premise
if bananas_per_friend_hypothesis!= total_bananas_premise:
    # check if the number of bananas each friend gets in the hypothesis contradicts the number of bananas in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
