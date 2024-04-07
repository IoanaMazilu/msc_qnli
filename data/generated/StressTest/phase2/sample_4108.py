# Premise: Martin bought less than 20 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: neutral

tickets_bought_premise = 20
tickets_bought_hypothesis = 10
full_price_ticket = 2.00
discounted_price_ticket = 1.60

# the hypothesis refers to the number of tickets bought by Martin and the prices of the tickets mentioned in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tickets_bought_premise'
    label = "contradiction"
elif full_price_ticket != 2.00 or discounted_price_ticket != 1.60:
    # check if the prices of the tickets in the hypothesis contradict the prices mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

