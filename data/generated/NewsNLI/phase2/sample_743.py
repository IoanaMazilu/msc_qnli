# Premise: But in towns with populations under 10,000, murders saw a big jump.
# Hypothesis: Murders jumped more than 18% in towns with populations under 10,000.
# Golden Label: neutral

population_premise = 10000
population_hypothesis = 10000
murder_increase_hypothesis = 0.18

# the premise and the hypothesis both talk about the increase in murders in towns with populations under 10,000
# but the premise does not specify the percentage increase, hence we cannot entail or contradict the hypothesis
label = "neutral"

print(label)

