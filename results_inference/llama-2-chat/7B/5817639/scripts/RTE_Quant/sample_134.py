report_premise = 5
report_hypothesis = 200000

# the hypothesis talks about the number of people killed in an air attack, which is not referenced in the premise
# the hypothesis cannot be entailed from the premise, since the number of people killed is unknown
label = "neutral"

print(label)
