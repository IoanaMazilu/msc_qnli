passenger_cost_premise = 100000
passenger_cost_hypothesis = 100000

# the hypothesis mentions the cost of the trip for one passenger, which is also mentioned in the premise
# however, the hypothesis refers to a specific trip from Singapore to Sydney, which cannot be entailed from the premise
label = "neutral"

print(label)
