# Premise: How many liters of blue paint must be added to 16 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to 36 liters of Fuchsia to change it to Mauve paint?
# Golden Label: contradiction

fuchsia_paint_premise = 16
fuchsia_paint_hypothesis = 36

# the hypothesis is asking about a similar situation as the premise but with a different amount of Fuchsia paint
if fuchsia_paint_hypothesis == fuchsia_paint_premise:
    # check if the amount of Fuchsia paint in the hypothesis matches the amount in the premise
    label = "contradiction"
else:
    # the hypothesis does not contradict the premise, but the exact amount of blue paint needed cannot be inferred from the premise
    label = "neutral"

print(label)

