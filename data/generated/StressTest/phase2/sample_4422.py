# Premise: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought less than 50 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: entailment

tickets_premise = 10
tickets_hypothesis = 50

# the hypothesis talks about the number of concert tickets Martin bought, referenced also in the premise
if tickets_hypothesis >= tickets_premise:
    # check if the hypothesis value contradicts the exact number of 'tickets_premise'
    label = "contradiction"
else:
    # the premise gives only an exact number for the tickets
    # any number of tickets less than 'tickets_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)

