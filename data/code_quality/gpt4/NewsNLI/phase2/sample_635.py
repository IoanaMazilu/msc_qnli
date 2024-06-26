stranded_passengers_premise = 4000
stranded_passengers_hypothesis = 4000

# the hypothesis mentions the number of stranded passengers, which is also mentioned in the premise
# however, the hypothesis introduces new information about the reason (Air Australia running out of money), which cannot be entailed from the premise
label = "neutral"

print(label)
