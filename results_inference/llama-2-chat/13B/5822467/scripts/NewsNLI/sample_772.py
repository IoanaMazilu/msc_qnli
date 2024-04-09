unemployment_premise = 12.7
unemployment_hypothesis = 11.1

# the hypothesis mentions the unemployment rate in Kentucky, which is also mentioned in the premise

# check if the unemployment rate in the hypothesis is lower than the rate in the premise
if unemployment_hypothesis < unemployment_premise:
    # if the hypothesis unemployment rate is lower, we can infer entailment
    label = "entailment"
elif unemployment_hypothesis > unemployment_premise:
    # if the hypothesis unemployment rate is higher, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis unemployment rate is the same as the premise, we can infer neutrality
    label = "neutral"

print(label)
