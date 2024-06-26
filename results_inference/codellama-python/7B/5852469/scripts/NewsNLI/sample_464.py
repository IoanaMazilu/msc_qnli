growth_premise = 0.025
growth_hypothesis = 0.025
unemployment_rate_premise = 0.051
unemployment_rate_hypothesis = 0.051

# the hypothesis mentions the growth and the unemployment rate in the U.S., which are also mentioned in the premise
if growth_hypothesis!= growth_premise:
    # check if the growth in the hypothesis contradicts the growth reported in the premise
    label = "contradiction"
elif unemployment_rate_hypothesis!= unemployment_rate_premise:
    # check if the unemployment rate from the hypothesis contradicts the unemployment rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
