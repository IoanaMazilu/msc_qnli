# Premise: If there are less than 85 males altogether, how many gerbils does Claire have?
# Hypothesis: If there are 25 males altogether, how many gerbils does Claire have?
# Golden Label: neutral

males_premise = 85
males_hypothesis = 25

# the hypothesis refers to the number of males mentioned in the premise
if males_hypothesis >= males_premise:
    # check if the number of males in the hypothesis contradicts the estimate of less than 'males_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males less than 'males_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

