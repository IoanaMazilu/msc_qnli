diane_paint_premise = 2
diane_paint_hypothesis = 1

if diane_paint_hypothesis <= diane_paint_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
