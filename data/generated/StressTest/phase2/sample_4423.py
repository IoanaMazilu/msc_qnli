# Premise: Martin bought less than 50 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: neutral

tickets_bought_premise = 50
tickets_bought_hypothesis = 10

# the hypothesis refers to the number of tickets bought by Martin mentioned in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the number of tickets bought in the hypothesis contradicts the estimate of less than 'tickets_bought_premise'
    label = "contradiction"
elif tickets_bought_hypothesis < tickets_bought_premise:
    # any number of tickets less than 'tickets_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

