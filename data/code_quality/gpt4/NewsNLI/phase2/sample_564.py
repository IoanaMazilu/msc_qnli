british_citizens_premise = 1005
unredeemed_miles_percent_premise = 0.40

unredeemed_miles_percent_hypothesis = 0.40

# the hypothesis mentions the percentage of passengers who never redeem loyalty miles, which is also mentioned in the premise
# however, the hypothesis refers to a different population (all passengers), which cannot be entailed from the premise (British citizens only)
if unredeemed_miles_percent_hypothesis != unredeemed_miles_percent_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # the percentage is the same, but the population is different, so the relation is neutral
    label = "neutral"

print(label)
