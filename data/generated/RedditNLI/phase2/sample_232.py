# Premise: 64% of Americans say we have a poor economy.
# Hypothesis: 90% of Americans say economy stinks.
# Golden Label: contradiction

percentage_americans_premise = 64
percentage_americans_hypothesis = 90

# the hypothesis and premise mention the percentage of Americans who have a negative view of the economy
if percentage_americans_hypothesis > percentage_americans_premise:
    # check if the percentage of Americans in the hypothesis contradicts the percentage of Americans in the premise
    label = "contradiction"
else:
    # the premise gives a percentage for the negative view of the economy
    # any percentage in the hypothesis equal or less than 'percentage_americans_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

