customers_premise = 2000
customers_hypothesis = 2000

# the hypothesis mentions the number of customers without power, which is also mentioned in the premise
if customers_hypothesis!= customers_premise:
    # check if the number of customers without power in the hypothesis contradicts the number of customers without power in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
