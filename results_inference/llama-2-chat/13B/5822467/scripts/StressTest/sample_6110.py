level_1_graduates_premise = 15
level_more_than_1_graduates_hypothesis = 15

# the hypothesis refers to the percentage of sales staff with level more than 1 college degree
if level_1_graduates_premise == level_more_than_1_graduates_hypothesis:
    # the hypothesis value is consistent with the premise, and the entailment can be inferred
    label = "entailment"
elif level_1_graduates_premise < level_more_than_1_graduates_hypothesis:
    # the hypothesis value contradicts the premise, as more than 1 college degree is required
    label = "contradiction"
else:
    # the premise only mentions level-1 college graduates, so the hypothesis cannot be inferred from the premise
    label = "neutral"

print(label)
