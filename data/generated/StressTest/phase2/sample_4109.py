# Premise: Martin bought 10 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Hypothesis: Martin bought 70 concert tickets, some at the full price of $2.00 per ticket, and some at a discounted price of $1.60 per ticket.
# Golden Label: contradiction

tickets_bought_premise = 10
tickets_bought_hypothesis = 70

# the hypothesis talks about the number of bought concert tickets, referenced also in the premise
if tickets_bought_hypothesis != tickets_bought_premise:
    # check if the number of tickets bought in the hypothesis contradicts the number of tickets bought reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

