# Premise: The farmers reported that they harvest 45.0 sacks of apples from an orchard that comprises 8.0 sections, and the same amount of apples is harvested from each section.
# Hypothesis: 6.2 sacks are harvested from a section.
# Golden Label: contradiction

total_sacks_premise = 45.0
sections_premise = 8.0
sacks_per_section_hypothesis = 6.2

# the hypothesis refers to the number of sacks harvested from a section, which is also mentioned in the premise
# compute the sacks harvested per section in the premise
sacks_per_section_premise = total_sacks_premise / sections_premise
if sacks_per_section_hypothesis != sacks_per_section_premise:
    # check if the number of sacks per section in the hypothesis contradicts the number of sacks per section from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

