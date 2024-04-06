# Premise: Americans Taxed $400 Billion For Fiber Optic Internet That Doesnt Exist.
# Hypothesis: Americans Taxed $300 Millon For Fiber Optic Internet That Doesnt Exist.
# Golden Label: contradiction

tax_amount_premise = 400 * 1e9 # converting billion to the base unit
tax_amount_hypothesis = 300 * 1e6 # converting million to the base unit

# the hypothesis and premise mention the tax amount for fiber optic internet
if tax_amount_hypothesis > tax_amount_premise:
    # check if the tax amount in the hypothesis contradicts the one in the premise
    label = "contradiction"
elif tax_amount_hypothesis < tax_amount_premise:
    # check if the tax amount in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the tax amount in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

