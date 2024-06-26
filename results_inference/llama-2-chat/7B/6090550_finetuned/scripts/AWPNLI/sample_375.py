baked_cakes_premise = 5.0
sold_cakes_premise = 6.0
baked_cakes_yesterday = 3.0
total_cakes = baked_cakes_premise + sold_cakes_premise

# the hypothesis talks about the number of cakes left, which can be computed from the premise
# compute the number of cakes left from the premise
left_cakes = total_cakes - baked_cakes_yesterday

print(f"{left_cakes:.2f} cakes left")
