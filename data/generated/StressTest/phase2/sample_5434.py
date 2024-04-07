# Premise: Susan, Daisy and Tim need to be seated in less than 5 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, Daisy and Tim need to be seated in 3 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: neutral

chairs_premise = 5
chairs_hypothesis = 3

# the hypothesis refers to the number of chairs mentioned in the premise
if chairs_hypothesis >= chairs_premise:
    # check if the number of 'chairs_hypothesis' contradicts the estimate of less than 'chairs_premise'
    label = "contradiction"
elif chairs_hypothesis < 3:
    # check if the number of 'chairs_hypothesis' contradicts the minimum number of chairs needed for Susan, Daisy and Tim
    label = "contradiction"
else:
    # the premise gives only an limit for the number of chairs
    # the number of 'chairs_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

