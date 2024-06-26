premise = "Loan Scandal Costs Wells Fargo $1 Billion; None of Fine Goes to Victims-Truthdig."
hypothesis = "Wells Fargo Said to Be Target of $1 Billion U.S. Fine."

# define variables for the numerical entities in the premise and hypothesis
premise_amount = float(1000000000)  # $1 billion
premise_victims = int(0)

hypothesis_amount = float(1000000000)  # $1 billion
hypothesis_victims = int(0)

# extract the quantities from the premise and hypothesis
quantities = {
    "amount": premise_amount,
    "victims": premise_victims,
    "amount_hypothesis": hypothesis_amount,
    "victims_hypothesis": hypothesis_victims,
}

# compare the quantities
for quantity, value in quantities.items():
    if quantity == "amount":
        if value!= hypothesis_amount:
            label = "contradiction"
        else:
            label = "entailment"
    elif quantity == "victims":
        if value!= hypothesis_victims:
            label = "contradiction"
        else:
            label = "entailment"
    else:
        pass

print(label)
