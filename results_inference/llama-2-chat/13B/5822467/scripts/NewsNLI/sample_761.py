passenger_premise = 10000
passenger_hypothesis = 100000

# the hypothesis mentions the price paid by one passenger for the first Singapore to Sydney trip, which is not mentioned in the premise
# therefore, we cannot entail or contradict the hypothesis from the premise
label = "neutral"

print(label)
