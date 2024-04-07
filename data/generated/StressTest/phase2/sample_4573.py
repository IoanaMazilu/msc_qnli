# Premise: Susan, John, Daisy, Tim and Kim need to be seated in more than 4 identical chairs in straight line so that Susan is seated always left to Tim.
# Hypothesis: Susan, John, Daisy, Tim and Kim need to be seated in 5 identical chairs in straight line so that Susan is seated always left to Tim.
# Golden Label: neutral

chairs_needed_premise = 4
chairs_needed_hypothesis = 5

# the hypothesis is talking about the number of chairs needed for seating, which is also referenced in the premise
if chairs_needed_hypothesis <= chairs_needed_premise:
    # check if the hypothesis number contradicts the estimate of more than 'chairs_needed_premise'
    label = "contradiction"
elif chairs_needed_hypothesis > chairs_needed_premise:
    # the premise gives only an estimate for the number of chairs
    # any number of chairs greater than 'chairs_needed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

