# Define variables for the numerical entities in the premise and hypothesis
kiwi_fruit_bought_premise = 8
kiwi_fruit_bought_hypothesis = 8
kiwi_fruit_rate_premise = 360
kiwi_fruit_rate_hypothesis = 360

# Check if the hypothesis value contradicts the premise value
if kiwi_fruit_bought_hypothesis <= kiwi_fruit_bought_premise:
    # The hypothesis value is less than or equal to the premise value, so the hypothesis is not entailed from the premise
    label = "contradiction"
else:
    # The hypothesis value is greater than the premise value, so the hypothesis is entailed from the premise
    label = "entailment"

print(label)
