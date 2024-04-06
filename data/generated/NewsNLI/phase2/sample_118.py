# Premise: Another is Erie, Pennsylvania, where snowfalls totals along the southern side of Lake Erie could reach 16 inches, Morris said.
# Hypothesis: Up to 16 inches of snow possible in some parts of the Northeast.
# Golden Label: entailment

snowfall_premise = 16
snowfall_hypothesis = 16

# the hypothesis mentions the amount of snowfall, which is also referenced in the premise
# however, the premise refers to the snowfall in Erie, Pennsylvania, while the hypothesis refers to the snowfall in some parts of the Northeast
# this information from the hypothesis cannot be fully and explicitly entailed from the premise
label = "neutral"

print(label)

