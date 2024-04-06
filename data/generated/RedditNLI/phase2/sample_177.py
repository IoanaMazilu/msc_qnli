# Premise: U.S. second-quarter GDP revised to show larger 3.7% gain.
# Hypothesis: U.S. economy grew 3.7 percent in second quarter.
# Golden Label: entailment

gdp_gain_premise = 3.7
gdp_gain_hypothesis = 3.7

# the hypothesis and premise both mention the GDP gain in the U.S. in the second quarter
if gdp_gain_hypothesis != gdp_gain_premise:
    # check if the GDP gain in the hypothesis contradicts the GDP gain in the premise
    label = "contradiction"
else:
    # if the GDP gain in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

