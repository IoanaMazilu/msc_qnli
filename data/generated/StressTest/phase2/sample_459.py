# Premise: Susan, Tim, Matt and Kim need to be seated in 4 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, Tim, Matt and Kim need to be seated in more than 2 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: entailment

chairs_premise = 4
chairs_hypothesis = 2

# The hypothesis talks about the number of chairs mentioned in the premise
if chairs_hypothesis >= chairs_premise:
    # check if the estimate of 'chairs_hypothesis' contradicts the number of chairs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

