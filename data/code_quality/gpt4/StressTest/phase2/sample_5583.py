fuchsia_liters_premise = 24
fuchsia_liters_hypothesis = 84

# the hypothesis refers to the same situation as the premise, but with a different quantity of Fuchsia paint
if fuchsia_liters_premise >= fuchsia_liters_hypothesis:
    # check if the quantity of Fuchsia paint in the premise contradicts the lower limit established by the hypothesis
    label = "contradiction"
else:
    # the hypothesis estimate is greater than the premise one, but it does not specify a particular quantity, just a maximum limit
    # therefore, entailment cannot be inferred directly
    label = "neutral"

print(label)
