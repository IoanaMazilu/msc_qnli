# Premise: All six British soldiers were charged with third-degree assault, Antonetti said.
# Hypothesis: Six British soldiers were arrested after a fight outside a Manhattan bar.
# Golden Label: neutral

soldiers_premise = 6
soldiers_hypothesis = 6

# the hypothesis mentions the arrest of British soldiers, which is also referenced in the premise
# however, the hypothesis refers to the location and situation of the arrest, which cannot be entailed from the premise
label = "neutral"

print(label)

