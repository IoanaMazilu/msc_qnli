# Premise: The less than 81 parents participating in the Smithville PTA have been assigned to at least 1 of 3 committees:festival planning, classroom aid, and teacher relations.
# Hypothesis: The 41 parents participating in the Smithville PTA have been assigned to at least 1 of 3 committees:festival planning, classroom aid, and teacher relations.
# Golden Label: neutral

parents_premise = 81
parents_hypothesis = 41

# the hypothesis refers to the number of parents participating in the PTA, which is also mentioned in the premise
if parents_hypothesis >= parents_premise:
    # check if the number of parents in the hypothesis contradicts the estimate of less than 'parents_premise'
    label = "contradiction"
else:
    # the number of parents in the hypothesis does not contradict the premise, but it can't be fully entailed from the premise
    label = "neutral"

print(label)

