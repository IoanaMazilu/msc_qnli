# Premise: How many liters of blue paint must be added to less than 60 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to 40 liters of Fuchsia to change it to Mauve paint?
# Golden Label: neutral

fuchsia_premise = 60
fuchsia_hypothesis = 40

# the hypothesis refers to the same amount of Fuchsia paint mentioned in the premise
if fuchsia_hypothesis >= fuchsia_premise:
    # check if the 'fuchsia_hypothesis' contradicts the 'fuchsia_premise' of less than 60 liters
    label = "contradiction"
elif fuchsia_hypothesis < fuchsia_premise:
    # the premise gives an upper bound for the amount of Fuchsia paint
    # any amount of Fuchsia paint less than 'fuchsia_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

