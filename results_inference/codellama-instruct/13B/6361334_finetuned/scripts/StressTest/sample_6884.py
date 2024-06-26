bonds_purchased_premise = 50
bonds_purchased_hypothesis = 70

# the hypothesis refers to the number of US saving bonds that Robert purchased
# the premise mentions that bonds are sold in $50 or $100 denominations only
# the hypothesis mentions that bonds are sold in $70 or $100 denominations only
# the hypothesis contradicts the premise, as it mentions a different denomination

if bonds_purchased_hypothesis!= bonds_purchased_premise:
    # check if the number of bonds purchased in the hypothesis contradicts the number of bonds purchased in the premise
    label = "contradiction"
else:
    # if the number of bonds purchased in the hypothesis does not contradict the number of bonds purchased in the premise, we can infer entailment
    label = "entailment"

print(label)
