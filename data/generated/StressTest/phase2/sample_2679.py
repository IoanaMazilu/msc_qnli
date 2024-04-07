# Premise: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought less than 40 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: entailment

tickets_bought_premise = 10
tickets_bought_hypothesis = 40

# the hypothesis refers to the number of tickets bought by Martin, which is also mentioned in the premise
if tickets_bought_hypothesis > tickets_bought_premise:
    # check if the hypothesis value contradicts the number of tickets bought in the premise
    label = "contradiction"
elif tickets_bought_hypothesis < tickets_bought_premise:
    # if the hypothesis values is less than the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)

