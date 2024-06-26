tickets_purchased_premise = 10
tickets_purchased_hypothesis = 30
full_price = 2.00
discounted_price = 1.60

# the hypothesis refers to the number of tickets bought by Martin, mentioned in the premise
if tickets_purchased_hypothesis != tickets_purchased_premise:
    # check if the number of tickets in the hypothesis contradicts the number of tickets bought in the premise
    label = "contradiction"
else:
    # if the number of tickets bought in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
