unemployment_rate_premise = 0.127
unemployment_rate_hypothesis = 0.111

# the hypothesis mentions the unemployment rate in Kentucky, which is not the same location as in the premise (Perry County, Hazard)
# thus, we cannot directly compare the unemployment rates from different states
label = "neutral"

print(label)
