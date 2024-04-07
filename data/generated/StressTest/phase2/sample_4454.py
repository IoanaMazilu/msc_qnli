# Premise: Susan, John, Peter, Jack, Daisy, Tim, Matt and Kim need to be seated in 8 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, John, Peter, Jack, Daisy, Tim, Matt and Kim need to be seated in 3 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: contradiction

chairs_premise = 8
chairs_hypothesis = 3

# the hypothesis refers to the number of chairs mentioned in the premise
if chairs_hypothesis != chairs_premise:
    # check if the number of chairs in the hypothesis contradicts the number of chairs reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

