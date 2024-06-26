passenger_premise = 1
passenger_hypothesis = 1
price_premise = 100000
price_hypothesis = 100000

# the hypothesis mentions the price paid by one passenger for the first Singapore to Sydney trip, which is also mentioned in the premise
# however, the hypothesis does not mention the majority of passengers paying between $1,500 and $5,000, which cannot be entailed from the premise
label = "neutral"

print(label)
