# Premise: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought less than 80 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: entailment

tickets_bought_premise = 10
tickets_bought_hypothesis = 80
full_price = 2.00
discount_price = 1.60

# the hypothesis talks about the number of tickets bought by Martin, referenced also in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the hypothesis value contradicts the number of tickets bought in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of tickets bought
    # any number of tickets less than 'tickets_bought_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)

