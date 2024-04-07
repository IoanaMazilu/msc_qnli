# Premise: Martin bought less than 80 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: neutral

tickets_bought_premise = 80
tickets_bought_hypothesis = 10

# the hypothesis talks about the number of concert tickets bought by Martin, which is also referenced in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the number of tickets bought in the hypothesis contradicts the estimate of less than 'tickets_bought_premise'
    label = "contradiction"
elif tickets_bought_hypothesis < tickets_bought_premise:
    # if the number of tickets bought in the hypothesis is less than the number of tickets mentioned in the premise, then it can be fully entailed from the premise
    label = "entailment"
else:
    # if the number of tickets bought in the hypothesis neither contradicts nor is explicitly entailed by the premise, then the relation is neutral
    label = "neutral"

print(label)

