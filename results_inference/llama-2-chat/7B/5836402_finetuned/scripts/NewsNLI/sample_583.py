hotels_premise = 0
hotels_hypothesis = 0
price_premise = 200
price_hypothesis = 200

# the hypothesis mentions the number of beachfront hotels under $200 in California, which is also referenced in the premise
# however, the hypothesis does not specify the total number of beachfront hotels in the U.S., which is mentioned in the premise
# therefore, we cannot infer entailment or contradiction based on this information
label = "neutral"

print(label)
