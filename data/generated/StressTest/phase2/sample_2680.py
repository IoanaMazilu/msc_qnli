# Premise: Martin bought less than 40 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: neutral

tickets_bought_premise = 40
tickets_bought_hypothesis = 10
full_price_ticket = 2.00
discounted_price_ticket = 1.60

# the hypothesis talks about the number of tickets bought by Martin, referenced also in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the hypothesis value contradicts the estimate of less than 'tickets_bought_premise'
    label = "contradiction"
elif tickets_bought_hypothesis < tickets_bought_premise:
    # the premise gives only an estimate for the number of tickets
    # any number of tickets less than 'tickets_bought_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

