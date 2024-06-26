diane_paint_premise = 1
diane_paint_hypothesis = 0.5

if diane_paint_hypothesis >= diane_paint_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
