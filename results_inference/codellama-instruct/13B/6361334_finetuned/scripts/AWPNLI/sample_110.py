apples_premise = 9.0
erasers_premise = 12.0
friends_premise = 3.0
apples_per_friend_hypothesis = 3.0

# the hypothesis refers to the number of apples each friend received, which are also mentioned in the premise
# compute the total number of apples in the premise
total_apples_premise = apples_premise / friends_premise
if total_apples_premise!= apples_per_friend_hypothesis:
    # check if the number of apples per friend in the hypothesis contradicts the number of apples from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
