# Premise: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought less than 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: contradiction

tickets_bought_premise = 10
tickets_bought_hypothesis = 10

# the hypothesis refers to the number of tickets bought by Martin, mentioned in the premise
if tickets_bought_hypothesis >= tickets_bought_premise:
    # check if the hypothesis contradicts the premise about the number of tickets bought
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)

