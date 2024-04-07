# Premise: How many liters of blue paint must be added to less than 54 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to 24 liters of Fuchsia to change it to Mauve paint?
# Golden Label: neutral

fuchsia_premise = 54
fuchsia_hypothesis = 24

# the hypothesis refers to the amount of Fuchsia mentioned in the premise
if fuchsia_hypothesis >= fuchsia_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fuchsia_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of Fuchsia
    # any amount of Fuchsia less than 'fuchsia_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

