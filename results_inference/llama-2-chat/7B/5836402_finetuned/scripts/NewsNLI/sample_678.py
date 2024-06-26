minor_injuries_premise = 100
serious_injuries_hypothesis = 2

# the hypothesis mentions the number of people being treated for serious injuries, which cannot be entailed from the premise
# the premise does not mention anything about the number of people being treated for minor injuries, which is the only information we can compare with the hypothesis
# however, the hypothesis refers to the number of serious injuries, which contradicts the premise
label = "contradiction"

print(label)
