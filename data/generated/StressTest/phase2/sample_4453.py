# Premise: Susan, John, Peter, Jack, Daisy, Tim, Matt and Kim need to be seated in more than 4 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, John, Peter, Jack, Daisy, Tim, Matt and Kim need to be seated in 8 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: neutral

chairs_premise = 4
chairs_hypothesis = 8

# the hypothesis refers to the number of chairs mentioned in the premise
if chairs_hypothesis <= chairs_premise:
    # check if the number of 'chairs_hypothesis' contradicts the estimate of more than 'chairs_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of chairs
    # any number of chairs greater than 'chairs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

