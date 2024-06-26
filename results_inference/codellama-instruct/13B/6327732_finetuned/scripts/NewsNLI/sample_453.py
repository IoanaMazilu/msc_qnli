range_premise = 60
range_hypothesis = 37

# the hypothesis mentions the range of the rockets, which is also mentioned in the premise
# however, the hypothesis refers to the range in miles, while the premise refers to the range in km
# this difference cannot be entailed from the premise, so we infer neutrality
label = "neutral"

print(label)
