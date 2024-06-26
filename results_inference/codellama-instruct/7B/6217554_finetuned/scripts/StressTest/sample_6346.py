investment_premise = 10000
investment_hypothesis = 50000

if investment_hypothesis <= investment_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
