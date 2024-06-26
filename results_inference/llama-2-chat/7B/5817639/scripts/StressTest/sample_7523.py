friends_premise = 6
friends_hypothesis = 5

# the hypothesis talks about the number of friends who want to ride in John's new car
if friends_hypothesis <= friends_premise:
    # check if the hypothesis value contradicts the estimate of 'friends_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the number of friends, but the hypothesis provides a specific value that is consistent with the premise
    label = "entailment"

print(label)
