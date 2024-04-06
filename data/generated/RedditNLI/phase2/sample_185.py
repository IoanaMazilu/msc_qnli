# Premise: Retail sales post biggest drop in 9 months.
# Hypothesis: Producer prices post biggest drop in 10 months.
# Golden Label: neutral

months_drop_premise = 9
months_drop_hypothesis = 10

# the hypothesis and premise mention the time period of the biggest drop, but in different contexts (retail sales vs producer prices)
# hence, we cannot compare these two directly
label = "neutral"

print(label)

