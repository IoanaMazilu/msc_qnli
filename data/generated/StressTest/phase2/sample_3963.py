# Premise: The 41 parents participating in the Smithville PTA have been assigned to at least 1 of 3 committees:festival planning, classroom aid, and teacher relations.
# Hypothesis: The less than 81 parents participating in the Smithville PTA have been assigned to at least 1 of 3 committees:festival planning, classroom aid, and teacher relations.
# Golden Label: entailment

parents_premise = 41
parents_hypothesis = 81

# the hypothesis refers to the number of parents participating in the Smithville PTA mentioned in the premise
if parents_hypothesis <= parents_premise:
    # check if the hypothesis estimate contradicts the number of parents in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

