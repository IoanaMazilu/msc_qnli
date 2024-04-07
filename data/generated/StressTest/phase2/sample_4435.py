# Premise: How many liters of blue paint must be added to less than 62 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to 32 liters of Fuchsia to change it to Mauve paint?
# Golden Label: neutral

fuchsia_premise = 62
fuchsia_hypothesis = 32

# the hypothesis talks about the number of liters of Fuchsia paint, referenced also in the premise
if fuchsia_hypothesis >= fuchsia_premise:
    # check if the hypothesis value contradicts the estimate of less than 'fuchsia_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of liters of Fuchsia paint
    # any number of liters less than 'fuchsia_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

