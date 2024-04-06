# Premise: The European Commission is providing 30 million euros ($39 million) to help the people affected by the flooding.
# Hypothesis: U.N. says nearly 1 million affected by flooding.
# Golden Label: neutral

funding_premise = 30
funding_hypothesis = 39
affected_people_hypothesis = 1000000

# the hypothesis mentions the number of people affected by flooding, which is not mentioned in the premise
# there is no information in the premise about the number of people affected by flooding
# also, there is no information in the hypothesis about the funding provided by the European Commission
# therefore, we cannot verify the information in the hypothesis based on the premise
label = "neutral"

print(label)

