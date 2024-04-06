# Premise: The fully functional submarine was built at a drydock at a clandestine complex that housed 50 people, said Jay Bergman, Andean regional director for the DEA.
# Hypothesis: The $4 million vessel was built at a clandestine complex.
# Golden Label: neutral

people_premise = 50
vessel_cost_hypothesis = 4000000

# the hypothesis mentions the construction of a vessel at a clandestine complex, which is also mentioned in the premise
# however, the hypothesis refers to the cost of the vessel which cannot be entailed from the premise
label = "neutral"

print(label)

