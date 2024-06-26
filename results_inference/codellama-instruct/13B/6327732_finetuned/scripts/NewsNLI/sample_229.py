wounded_premise = 1000
wounded_hypothesis = 6000
killed_premise = 1
killed_hypothesis = 6

# the hypothesis mentions the number of wounded and killed, which are also mentioned in the premise
# however, the hypothesis mentions a higher number of wounded and killed, which cannot be entailed from the premise
label = "contradiction"

print(label)
