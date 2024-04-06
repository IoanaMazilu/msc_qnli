# Premise: Officials said three people were killed in the blast in Damaturu, a northern town in Yobe state, John said.
# Hypothesis: 32 were killed in Madalla, a government official says.
# Golden Label: neutral

people_killed_premise = 3
people_killed_hypothesis = 32

# the hypothesis mentions the number of people killed in Madalla, which contradicts the number of people killed in Damaturu from the premise
if people_killed_hypothesis != people_killed_premise:
    label = "contradiction"
else:
    # if the two numbers do not contradict each other, we cannot infer any entailment because the locations are different
    label = "neutral"

print(label)

