# Premise: Julie has 7 friends.
# Hypothesis: Julie has more than 5 friends.
# Golden Label: entailment

friends_premise = 7
friends_hypothesis = 5

# the hypothesis talks about the number of friends Julie has, which is also mentioned in the premise
if friends_premise <= friends_hypothesis:
    # check if the number of friends in the premise contradicts the hypothesis estimate of more than 'friends_hypothesis'
    label = "contradiction"
else:
    # if the number of friends in the premise is more than 'friends_hypothesis', we can infer entailment
    label = "entailment"

print(label)

