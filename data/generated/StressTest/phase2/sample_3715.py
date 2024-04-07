# Premise: Shop Offered less than 50% offer for every Shirt, Smith bought a shirt at Rs.
# Hypothesis: Shop Offered 20% offer for every Shirt, Smith bought a shirt at Rs.
# Golden Label: neutral

shirt_discount_premise = 50
shirt_discount_hypothesis = 20

# the hypothesis refers to the discount percentage for shirts offered by the shop, as mentioned in the premise
if shirt_discount_hypothesis >= shirt_discount_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'shirt_discount_premise' percent
    label = "contradiction"
elif shirt_discount_hypothesis < shirt_discount_premise:
    # if the discount percentage in the hypothesis is less than the discount percentage in the premise
    # this is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

