# Premise: If there are less than 45 males altogether, how many gerbils does Claire have?
# Hypothesis: If there are 25 males altogether, how many gerbils does Claire have?
# Golden Label: neutral

males_premise = 45
males_hypothesis = 25

# the hypothesis refers to the premise condition about the number of males
if males_hypothesis >= males_premise:
    # check if the hypothesis contradicts the premise's condition of less than 'males_premise' males
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of males
    # any number of males less than 'males_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

