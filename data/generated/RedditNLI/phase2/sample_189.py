# Premise: U.S. GDP Growth Revised Down to 2.2% Rate in First Quarter.
# Hypothesis: US first-quarter growth revised down to 2.2%.
# Golden Label: entailment

gdp_growth_rate_premise = 2.2
gdp_growth_rate_hypothesis = 2.2

# the hypothesis and premise mention the GDP growth rate of the US in the first quarter
if gdp_growth_rate_hypothesis != gdp_growth_rate_premise:
    # check if the GDP growth rate in the hypothesis contradicts the GDP growth rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

