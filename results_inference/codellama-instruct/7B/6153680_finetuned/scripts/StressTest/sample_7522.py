friends_premise = 5
friends_hypothesis = 6

# the hypothesis talks about the number of friends who want to ride in John's car, referenced also in the premise
if friends_hypothesis <= friends_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
