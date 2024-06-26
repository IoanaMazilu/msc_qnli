skittles_premise = 40.0
friends_premise = 5.0
skittles_per_friend_hypothesis = 8.0

# the hypothesis refers to the number of Skittles each friend got, which can be computed from the premise
# compute the number of Skittles each friend got in the premise
skittles_per_friend_premise = skittles_premise / friends_premise
if skittles_per_friend_hypothesis != skittles_per_friend_premise:
    # check if the number of Skittles per friend in the hypothesis contradicts the number of Skittles per friend from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
