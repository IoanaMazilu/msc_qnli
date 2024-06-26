friends_premise = 5
friends_hypothesis = 6

# the hypothesis talks about the number of friends John has, which is also referenced in the premise
if friends_hypothesis!= friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends in the premise
    label = "contradiction"
else:
    # if the number of friends in the hypothesis does not contradict the number of friends in the premise, we can infer entailment
    label = "entailment"

print(label)
