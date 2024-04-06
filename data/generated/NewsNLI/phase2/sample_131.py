# Premise: (CNN) -- One tornado stayed on the ground for 95 miles as it tore through towns in Kentucky and West Virginia.
# Hypothesis: A twister that hit West Liberty, Kentucky, stayed on the ground for 95 miles.
# Golden Label: entailment

tornado_path_premise = 95
tornado_path_hypothesis = 95

# the hypothesis mentions the path length of a tornado, which is also mentioned in the premise
# however, the hypothesis refers to a specific location (West Liberty, Kentucky), which cannot be entailed from the premise
label = "neutral"

print(label)

