passenger_premise = 100000
passenger_hypothesis = 100000

# the hypothesis mentions the cost of the first Singapore to Sydney trip, which is also mentioned in the premise
# however, the hypothesis does not provide any information about the majority of passengers paying between $1,500 and $5,000
# therefore, we cannot infer entailment or contradiction
label = "neutral"

print(label)
