# Premise: If there are 25 males altogether, how many gerbils does Claire have?
# Hypothesis: If there are less than 35 males altogether, how many gerbils does Claire have?
# Golden Label: entailment

males_premise = 25
males_hypothesis = 35

# the hypothesis refers to the number of males mentioned in the premise
if males_hypothesis <= males_premise:
    # check if the estimate of 'males_hypothesis' contradicts the number of males in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of males, while the hypothesis gives an upper boundary
    # the premise does not contradict the hypothesis, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

