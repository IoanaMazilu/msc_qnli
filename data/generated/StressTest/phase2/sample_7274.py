# Premise: Kyle is a lumberjack with 12 trees to cut down.
# Hypothesis: Kyle is a lumberjack with more than 12 trees to cut down.
# Golden Label: contradiction

trees_premise = 12
trees_hypothesis = 12

# the hypothesis refers to the number of trees mentioned in the premise
if trees_hypothesis >= trees_premise:
    # check if the number of trees in the hypothesis contradicts the number of trees mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

