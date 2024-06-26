outstanding_fines_min_premise = 10000
outstanding_fines_max_premise = 29000000
outstanding_fines_max_hypothesis = 4500000

# the hypothesis mentions the maximum amount of outstanding fines, which is also referenced in the premise
# however, the hypothesis refers to this amount in US dollars, which cannot be entailed from the premise
label = "neutral"

print(label)
