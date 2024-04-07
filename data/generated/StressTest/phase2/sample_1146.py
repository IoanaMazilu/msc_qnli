# Premise: If there are 25 males altogether, how many gerbils does Claire have?
# Hypothesis: If there are less than 65 males altogether, how many gerbils does Claire have?
# Golden Label: entailment

males_premise = 25
males_hypothesis = 65

# the hypothesis refers to the number of males mentioned in the premise
if males_premise >= males_hypothesis:
    # check if the number of males in the premise contradicts the condition in the hypothesis
    label = "contradiction"
elif males_premise < males_hypothesis:
    # the premise gives a specific number for the males
    # any number of males less than 'males_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

