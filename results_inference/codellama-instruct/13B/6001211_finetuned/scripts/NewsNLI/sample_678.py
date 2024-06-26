minor_injuries_premise = 100
serious_injuries_hypothesis = 2

# the hypothesis mentions the number of people being treated for serious injuries, which is not referenced in the premise
# the premise mentions the number of people being treated for minor injuries, which is not referenced in the hypothesis
# there is no numerical information in the hypothesis that can be compared to the premise
label = "neutral"

print(label)
