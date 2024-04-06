# Premise: US GDP growth slows to 1.8%, (no) surprise jump in jobless rate.
# Hypothesis: U.S. Economic Growth Slows to 1.8% Rate in Quarter.
# Golden Label: neutral

gdp_growth_premise = 1.8
gdp_growth_hypothesis = 1.8

# the hypothesis and premise mention the same GDP growth rate
if gdp_growth_hypothesis != gdp_growth_premise:
    # check if the GDP growth rate in the hypothesis contradicts the GDP growth rate in the premise
    label = "contradiction"
else:
    # the GDP growth rate in the hypothesis does not contradict the one in the premise and can be explicitly entailed from it
    label = "entailment"

print(label)

