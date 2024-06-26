bananas_premise = 21.0
friends_premise = 3.0
bananas_hypothesis = 2.0

# the hypothesis refers to the number of bananas each friend gets, which are also mentioned in the premise
# compute the total number of bananas each friend gets from the premise
bananas_per_friend = bananas_premise / friends_premise
if bananas_hypothesis!= bananas_per_friend:
    # check if the number of bananas each friend gets from the hypothesis contradicts the number of bananas each friend gets from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
