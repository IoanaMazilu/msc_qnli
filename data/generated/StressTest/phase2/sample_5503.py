# Premise: Susan, John, Daisy, Tim, Matt, Jane and Kim need to be seated in more than 1 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, John, Daisy, Tim, Matt, Jane and Kim need to be seated in 7 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: neutral

chairs_premise = 1
chairs_hypothesis = 7

# the hypothesis refers to the number of chairs mentioned in the premise
if chairs_hypothesis <= chairs_premise:
    # check if the number of 'chairs_hypothesis' contradicts the number of chairs in the premise
    label = "contradiction"
elif chairs_hypothesis > chairs_premise:
    # check if the number of 'chairs_hypothesis' is more than the number of chairs in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

