# Premise: At least one couple has tied the knot.
# Hypothesis: There has been at least one wedding in the park.
# Golden Label: entailment

weddings_premise = 1
weddings_hypothesis = 1

# the hypothesis mentions that at least one wedding has happened, which is also referenced in the premise
# however, the hypothesis refers to the location of the wedding which cannot be entailed from the premise
label = "neutral"

print(label)

