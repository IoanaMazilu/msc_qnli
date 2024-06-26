fines_premise_low = 10000
fines_premise_high = 29000000
fines_hypothesis = 4500000

# the hypothesis mentions the total amount of outstanding fines, which is also referenced in the premise
# however, the hypothesis does not specify the lower limit of the range, which cannot be entailed from the premise
label = "neutral"

print(label)
