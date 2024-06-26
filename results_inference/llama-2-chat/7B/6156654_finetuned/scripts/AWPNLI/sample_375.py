baked_cakes_premise = 5.0
sold_cakes_premise = 6.0
baked_cakes_yesterday = 3.0

# the hypothesis refers to the number of cakes left, which can be calculated based on the premise
# the hypothesis value is less than the baked cakes yesterday, which is a contradiction to the premise
# therefore, the hypothesis is a contradiction to the premise

print("entailment" if (baked_cakes_premise - baked_cakes_yesterday) >= 0 else "contradiction")
