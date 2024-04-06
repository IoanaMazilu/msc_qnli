# Premise: The plush shopping center is the latest addition to Yas Island, a purpose-built $40 billion holiday destination rising off the coast of Abu Dhabi.
# Hypothesis: Part of $40b Yas Island entertainment center, including F1 circuit.
# Golden Label: neutral

cost_premise = 40e9
cost_hypothesis = 40e9

# the hypothesis mentions the cost of Yas Island, which is also referenced in the premise
# however, the hypothesis adds information about the F1 circuit, which cannot be entailed from the premise
label = "neutral"

print(label)

