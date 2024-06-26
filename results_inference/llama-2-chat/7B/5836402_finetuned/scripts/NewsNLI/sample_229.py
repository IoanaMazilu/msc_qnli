killed_premise = 1
wounded_premise = 1000
killed_hypothesis = 6
wounded_hypothesis = 1000

# the hypothesis mentions the number of people killed and wounded, which are also referenced in the premise
# however, the hypothesis refers to recent demonstrations, which cannot be entailed from the premise
label = "neutral"

print(label)
