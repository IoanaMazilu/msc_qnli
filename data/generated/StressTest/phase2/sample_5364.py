# Premise: Victor has 15 cups if flour, 16 cups of sugar and 8 cups of milk.
# Hypothesis: Victor has less than 55 cups if flour, 16 cups of sugar and 8 cups of milk.
# Golden Label: entailment

flour_cups_premise = 15
flour_cups_hypothesis = 55
sugar_cups_premise = 16
sugar_cups_hypothesis = 16
milk_cups_premise = 8
milk_cups_hypothesis = 8

# the hypothesis refers to the number of cups of each ingredient Victor has
if flour_cups_hypothesis <= flour_cups_premise:
    # check if the hypothesis value contradicts the exact number of flour cups in the premise
    label = "contradiction"
elif sugar_cups_hypothesis != sugar_cups_premise:
    # check if the number of sugar cups in the hypothesis contradicts the number of sugar cups in the premise
    label = "contradiction"
elif milk_cups_hypothesis != milk_cups_premise:
    # check if the number of milk cups in the hypothesis contradicts the number of milk cups in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

