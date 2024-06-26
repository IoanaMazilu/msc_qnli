months_joined_premise = 2
months_joined_hypothesis = 4

# the hypothesis refers to the number of months Jose joined him, which is also mentioned in the premise
if months_joined_hypothesis <= months_joined_premise:
    # check if the hypothesis value contradicts the exact number of 'months_joined_premise'
    label = "contradiction"
elif months_joined_premise != months_joined_hypothesis:
    # any number of months less than 'months_joined_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
