# Premise: Diane find less than 2 can of paint are just enough to paint one third of her room.
# Hypothesis: Diane find 1 can of paint are just enough to paint one third of her room.
# Golden Label: neutral

cans_paint_premise = 2
cans_paint_hypothesis = 1

# the hypothesis refers to the number of cans of paint used by Diane mentioned in the premise
if cans_paint_hypothesis >= cans_paint_premise:
    # check if the hypothesis value contradicts the estimate of less than 'cans_paint_premise'
    label = "contradiction"
elif cans_paint_hypothesis < cans_paint_premise:
    # any number of cans less than 'cans_paint_premise' is consistent with the premise
    # since the premise estimates less than 2 cans, 1 can can be explicitly entailed from the premise
    label = "entailment"

print(label)

