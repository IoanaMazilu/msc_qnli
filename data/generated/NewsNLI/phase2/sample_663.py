# Premise: Youth unemployment is at 19.9 percent in the eurozone and 20.5 percent in the wider European Union, it said.
# Hypothesis: 10 percent unemployment for eurozone, 9.7 percent for wider EU.
# Golden Label: neutral

unemployment_eurozone_premise = 19.9
unemployment_eu_premise = 20.5

unemployment_eurozone_hypothesis = 10
unemployment_eu_hypothesis = 9.7

# the hypothesis mentions the unemployment rates for eurozone and EU, which are also mentioned in the premise
if unemployment_eurozone_hypothesis != unemployment_eurozone_premise:
    # check if the eurozone unemployment rate in the hypothesis contradicts the eurozone unemployment rate reported in the premise
    label = "contradiction"
elif unemployment_eu_hypothesis != unemployment_eu_premise:
    # check if the EU unemployment rate from the hypothesis contradicts the EU unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

