bonds_purchase_premise = 1000
bonds_purchase_hypothesis = 8000

# the hypothesis refers to the amount of bonds Robert purchased, also mentioned in the premise
if bonds_purchase_hypothesis == bonds_purchase_premise:
    # check if the amount of bonds purchased in the hypothesis matches the amount stated in the premise
    label = "entailment"
elif bonds_purchase_hypothesis != bonds_purchase_premise:
    # check if the amount of bonds purchased in the hypothesis contradicts the amount stated in the premise
    label = "contradiction"

print(label)
