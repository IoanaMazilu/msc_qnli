# Premise: John has 6 people in his group of friends.
# Hypothesis: John has less than 7 people in his group of friends.
# Golden Label: entailment

group_size_premise = 6
group_size_hypothesis = 7

# the hypothesis refers to the size of John's group of friends, mentioned in the premise
if group_size_premise >= group_size_hypothesis:
    # check if the size of the group in the premise contradicts the hypothesis that the group has less than 'group_size_hypothesis' members
    label = "contradiction"
elif group_size_premise != group_size_hypothesis - 1:
    # check if the premise's group size is exactly one less than the 'group_size_hypothesis'
    # if it is not, it means the hypothesis cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the premise's group size is exactly one less than the 'group_size_hypothesis', we can infer entailment
    label = "entailment"

print(label)

