# Premise: If there are more than 15 males altogether, how many gerbils does Claire have?
# Hypothesis: If there are 25 males altogether, how many gerbils does Claire have?
# Golden Label: neutral

males_premise = 15
males_hypothesis = 25

# the hypothesis talks about the number of males, referenced also in the premise
if males_hypothesis <= males_premise:
    # check if the hypothesis value contradicts the estimate of more than 'males_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males greater than 'males_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

