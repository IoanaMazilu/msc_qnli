# Premise: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought less than 30 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: entailment

tickets_bought_premise = 10
tickets_bought_hypothesis = 30

# the hypothesis refers to the number of concert tickets Martin bought, which is also mentioned in the premise
if tickets_bought_hypothesis <= tickets_bought_premise:
    # check if the hypothesis value contradicts the number of tickets bought according to the premise
    label = "contradiction"
elif tickets_bought_hypothesis > tickets_bought_premise:
    # the premise gives an exact number of tickets bought
    # any number of tickets less than 'tickets_bought_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

