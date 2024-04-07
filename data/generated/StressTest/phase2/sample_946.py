# Premise: Victor has less than 35 cups if flour, 16 cups of sugar and 8 cups of milk.
# Hypothesis: Victor has 15 cups if flour, 16 cups of sugar and 8 cups of milk.
# Golden Label: neutral

flour_cups_premise = 35
flour_cups_hypothesis = 15
sugar_cups_premise = 16
sugar_cups_hypothesis = 16
milk_cups_premise = 8
milk_cups_hypothesis = 8

# the hypothesis refers to the quantities of flour, sugar and milk mentioned in the premise
if flour_cups_hypothesis >= flour_cups_premise:
    # check if the exact number of 'flour_cups_hypothesis' contradicts the estimate of less than 'flour_cups_premise'
    label = "contradiction"
elif sugar_cups_hypothesis != sugar_cups_premise or milk_cups_hypothesis != milk_cups_premise:
    # check if the number of sugar or milk cups in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

