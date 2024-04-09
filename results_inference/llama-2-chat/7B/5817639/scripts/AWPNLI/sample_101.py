bananas_premise = 21.0
friends_premise = 3.0
bananas_hypothesis = 2.0

# the hypothesis talks about the number of bananas each friend gets, which is also mentioned in the premise
# compute the total number of bananas each friend will get
total_bananas_per_friend = bananas_hypothesis * friends_hypothesis

# check if the total number of bananas each friend gets in the hypothesis contradicts the estimate from the premise
if total_bananas_per_friend!= bananas_premise / friends_premise:
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
