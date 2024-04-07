# Premise: Susan, John, Peter, Jack, Daisy, Tim, Matt and Kim need to be seated in 8 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, John, Peter, Jack, Daisy, Tim, Matt and Kim need to be seated in more than 4 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: entailment

chairs_premise = 8
chairs_hypothesis = 4

# the hypothesis refers to the number of chairs needed, which is also mentioned in the premise
if chairs_hypothesis >= chairs_premise:
    # check if the 'chairs_hypothesis' contradicts the number of chairs in the premise
    label = "contradiction"
elif chairs_hypothesis < chairs_premise:
    # check if the number of chairs in the hypothesis is less than in the premise
    # if it is less, then the premise cannot fully entail the hypothesis
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

