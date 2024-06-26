jobless_rate_premise = 0.127
jobless_rate_hypothesis = 0.111

# the hypothesis mentions the unemployment rate in Kentucky, which is not referenced in the premise
# however, the premise mentions the unemployment rate in Perry County, which cannot be entailed from the hypothesis
label = "neutral"

print(label)
