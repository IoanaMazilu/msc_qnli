# Premise: The 40 parents participating in the Smithville PTA have been assigned to at least 1 of 3 committees:festival planning, classroom aid, and teacher relations.
# Hypothesis: The less than 80 parents participating in the Smithville PTA have been assigned to at least 1 of 3 committees:festival planning, classroom aid, and teacher relations.
# Golden Label: entailment

parents_premise = 40
parents_hypothesis = 80

# the hypothesis refers to the number of parents participating in the Smithville PTA mentioned in the premise
if parents_hypothesis <= parents_premise:
    # check if the estimate of 'parents_hypothesis' contradicts the number of parents in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of parents
    # any number of parents less than 'parents_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

