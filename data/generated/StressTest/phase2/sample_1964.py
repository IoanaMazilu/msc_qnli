# Premise: How many liters of blue paint must be added to 40 liters of Fuchsia to change it to Mauve paint?
# Hypothesis: How many liters of blue paint must be added to 10 liters of Fuchsia to change it to Mauve paint?
# Golden Label: contradiction

fuchsia_liters_premise = 40
fuchsia_liters_hypothesis = 10

# the hypothesis refers to the amount of Fuchsia paint mentioned in the premise
if fuchsia_liters_hypothesis != fuchsia_liters_premise:
    # check if the amount of Fuchsia paint in the hypothesis contradicts the amount of Fuchsia paint in the premise
    label = "contradiction"
else:
    # if the amount of Fuchsia paint in the hypothesis and the premise are the same, we can infer entailment
    label = "entailment"

print(label)

