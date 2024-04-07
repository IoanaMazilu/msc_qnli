# Premise: Susan, Tim, Matt and Kim need to be seated in more than 2 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, Tim, Matt and Kim need to be seated in 4 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: neutral

chairs_needed_premise = 2
chairs_needed_hypothesis = 4

# The hypothesis refers to the number of identical chairs needed for seating Susan, Tim, Matt and Kim, referenced also in the premise
if chairs_needed_hypothesis <= chairs_needed_premise:
    # Check if the number of chairs in the hypothesis contradicts the estimate of more than 'chairs_needed_premise'
    label = "contradiction"
elif chairs_needed_hypothesis > chairs_needed_premise:
    # Any number of chairs greater than 'chairs_needed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

