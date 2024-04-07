# Premise: Jose joined him less than 3 months later, investing Rs.
# Hypothesis: Jose joined him 2 months later, investing Rs.
# Golden Label: neutral

months_joined_premise = 3
months_joined_hypothesis = 2

# the hypothesis talks about the time when Jose joined, referenced also in the premise
if months_joined_hypothesis >= months_joined_premise:
    # check if the hypothesis value contradicts the premise of joining less than 'months_joined_premise' later
    label = "contradiction"
elif months_joined_hypothesis < months_joined_premise:
    # the premise provides an upper bound for when Jose joined 
    # any number of months less than 'months_joined_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

