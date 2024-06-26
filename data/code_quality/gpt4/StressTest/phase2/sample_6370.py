cans_paint_premise = 8
cans_paint_hypothesis = 4

# the hypothesis refers to the number of cans of paint Diane used, which is also mentioned in the premise
if cans_paint_hypothesis >= cans_paint_premise:
    # check if the number of paint cans in the hypothesis contradicts the premise's estimate of less than 'cans_paint_premise'
    label = "contradiction"
elif cans_paint_hypothesis < cans_paint_premise:
    # if the number of paint cans in the hypothesis is less than 'cans_paint_premise', it can be directly entailed from the premise
    label = "entailment"

print(label)
