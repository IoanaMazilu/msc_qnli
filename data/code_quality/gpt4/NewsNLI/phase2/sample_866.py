funding_premise = 30
funding_hypothesis = 39
affected_people_hypothesis = 1000000

# the hypothesis mentions the number of people affected by flooding, which is not mentioned in the premise
# there is no information in the premise about the number of people affected by flooding
# also, there is no information in the hypothesis about the funding provided by the European Commission
# therefore, we cannot verify the information in the hypothesis based on the premise
label = "neutral"

print(label)
