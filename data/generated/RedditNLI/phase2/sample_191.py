# Premise: China economy grows 7 percent in third quarter, weakest since 2009.
# Hypothesis: China economy logs weakest growth since 2009.
# Golden Label: entailment

growth_rate_premise = 7
year_premise = 2009

# the hypothesis and premise mention the growth rate of China's economy and a reference year
# the hypothesis does not specify a numerical growth rate
# thus, it neither contradicts nor explicitly entails the premise
label = "neutral"

print(label)

