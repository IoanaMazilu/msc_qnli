friends_premise = 6
friends_hypothesis = 5

# the hypothesis refers to the number of friends wanting to ride in John's new car, which is also mentioned in the premise
if friends_hypothesis!= friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
