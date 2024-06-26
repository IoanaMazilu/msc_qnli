customers_premise = float(19.0)
customers_hypothesis = float(37.0)

# compare the number of customers in the premise and hypothesis
if customers_premise + customers_hypothesis - customers_premise >= 0:
    # if the total number of customers in the hypothesis is greater than or equal to the sum of the number of customers in the premise, we can infer entailment
    label = "entailment"
elif customers_hypothesis - customers_premise < 0:
    # if the number of customers in the hypothesis is less than the number of customers in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
