joined_later_premise = 2
joined_later_hypothesis = 8

# the hypothesis refers to the time Jose joined, mentioned in the premise
if joined_later_premise >= joined_later_hypothesis:
    # check if the premise estimate contradicts the hypothesis estimate
    label = "contradiction"
elif joined_later_premise < joined_later_hypothesis:
    # check if the premise estimate is less than the hypothesis estimate
    label = "entailment"
else:
    # if the premise and hypothesis estimates are equal, it's neutral
    label = "neutral"

print(label)
