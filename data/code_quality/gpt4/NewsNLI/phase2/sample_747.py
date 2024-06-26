west_ham_contribution_premise = 24000000
stadium_build_cost_premise = 690000000
reconstruction_cost_hypothesis_min = 210000000
reconstruction_cost_hypothesis_max = 240000000

# the hypothesis mentions the cost of reconstruction, which is not mentioned in the premise
# the premise mentions the cost of building the stadium, and West Ham's contribution, which are not mentioned in the hypothesis
# there is no numerical information that can be directly compared between the premise and the hypothesis
label = "neutral"

print(label)
