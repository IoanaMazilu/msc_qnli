# Premise: Susan, John, Daisy, Tim, Matt, Jane and Kim need to be seated in 7 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, John, Daisy, Tim, Matt, Jane and Kim need to be seated in less than 7 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: contradiction

chairs_premise = 7
chairs_hypothesis = 7

# the hypothesis refers to the number of chairs mentioned in the premise
if chairs_hypothesis >= chairs_premise:
    # check if the number of chairs in the hypothesis contradicts the number of chairs in the premise
    label = "contradiction"
else:
    # the premise gives exact number of chairs, whereas hypothesis gives lesser number
    # hence the hypothesis contradicts the premise
    label = "contradiction"

print(label)

