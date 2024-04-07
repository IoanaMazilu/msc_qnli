# Premise: How many liters of blue paint must be added to less than 86 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to 16 liters of Fuchsia to change it to Mauve paint?
# Golden Label: neutral

fuchsia_premise = 86
fuchsia_hypothesis = 16

# the hypothesis refers to the amount of Fuchsia paint mentioned in the premise
if fuchsia_hypothesis >= fuchsia_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fuchsia_premise'
    label = "contradiction"
elif fuchsia_hypothesis < fuchsia_premise:
    # the premise gives only an estimate for the amount of Fuchsia paint
    # any amount of Fuchsia paint less than 'fuchsia_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

