# Premise: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought 20 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: contradiction

tickets_bought_premise = 10
tickets_bought_hypothesis = 20
full_price = 2.00
discounted_price = 1.60

# the hypothesis refers to the number of tickets bought by Martin mentioned in the premise
if tickets_bought_hypothesis != tickets_bought_premise:
    # check if the number of tickets bought in the hypothesis contradicts the number of tickets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

