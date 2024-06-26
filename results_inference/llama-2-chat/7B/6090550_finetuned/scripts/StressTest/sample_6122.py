 price_premise = 4
price_hypothesis = 8

# the hypothesis talks about the number of returned t-shirts and the average price of the remaining ones, which are also mentioned in the premise
if price_hypothesis!= price_premise:
    # check if the number of returned t-shirts in the hypothesis contradicts the number of returned t-shirts in the premise
    label = "contradiction"
else:
    # if the number of returned t-shirts in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
