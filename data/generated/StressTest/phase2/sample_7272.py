# Premise: Kyle is a lumberjack with 12 trees to cut down.
# Hypothesis: Kyle is a lumberjack with less than 72 trees to cut down.
# Golden Label: entailment

trees_premise = 12
trees_hypothesis = 72

# the hypothesis refers to the same Kyle and his job as a lumberjack, and the number of trees he has to cut down
if trees_premise > trees_hypothesis:
    # check if the actual number of trees from the premise contradicts the estimate in the hypothesis
    label = "contradiction"
elif trees_premise == trees_hypothesis:
    # if the number of trees in the premise equals the number of trees in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # any number less than 'trees_hypothesis' is consistent with the hypothesis, but the exact number cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)

