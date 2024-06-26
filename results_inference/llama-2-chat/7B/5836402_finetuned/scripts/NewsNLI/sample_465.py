fines_premise = [10000, 2900000]
fines_hypothesis = 4500000

# the hypothesis mentions the upper limit of outstanding fines, which is also referenced in the premise
# however, the hypothesis refers to the upper limit in US dollars, which cannot be entailed from the premise
label = "neutral"

print(label)
