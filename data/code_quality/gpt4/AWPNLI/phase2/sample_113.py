total_skittles_premise = 40.0
shared_among_friends_premise = 5.0
skittles_per_friend_hypothesis = 12.0

# the hypothesis refers to the number of Skittles each friend got, which can be inferred from the premise
# compute the number of Skittles each friend got in the premise
skittles_per_friend_premise = total_skittles_premise / shared_among_friends_premise
if skittles_per_friend_hypothesis != skittles_per_friend_premise:
    # check if the number of Skittles each friend got in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
