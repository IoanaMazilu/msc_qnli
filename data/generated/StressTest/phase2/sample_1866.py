# Premise: How many liters of blue paint must be added to 24 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to less than 74 liters of Fuchsia to change it to Mauve paint?
# Golden Label: entailment

fuchsia_liters_premise = 24
fuchsia_liters_hypothesis = 74

# the hypothesis talks about the amount of Fuchsia paint in liters, also referenced in the premise
if fuchsia_liters_premise >= fuchsia_liters_hypothesis:
    # check if the value of 'fuchsia_liters_premise' contradicts the estimate of less than 'fuchsia_liters_hypothesis'
    label = "contradiction"
else:
    # the hypothesis gives only an estimate for the amount of Fuchsia paint
    # any amount of Fuchsia paint less than 'fuchsia_liters_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

