# Premise: A study has found nearly 200 new species of frogs in Madagascar.
# Hypothesis: Nearly 200 new species of amphibians found on biodiversity hotspot of Madagascar.
# Golden Label: entailment

new_species_premise = 200
new_species_hypothesis = 200

# the hypothesis mentions the number of new species found in Madagascar, which is also mentioned in the premise
# however, the hypothesis refers to amphibians in general, not specifically frogs, which cannot be entailed from the premise
label = "neutral"

print(label)

