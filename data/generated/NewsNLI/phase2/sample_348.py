# Premise: The four died when the part of the mall they were in collapsed, Maj. Emmanuel Chirchir said.
# Hypothesis: The four died when the part of the mall they were in collapsed, Kenyan military spokesman says.
# Golden Label: entailment

death_toll_premise = 4
death_toll_hypothesis = 4

# the hypothesis mentions the number of deaths due to the mall collapse, which is also mentioned in the premise
# however, the hypothesis refers to a Kenyan military spokesman, which cannot be entailed from the premise
label = "neutral"

print(label)

