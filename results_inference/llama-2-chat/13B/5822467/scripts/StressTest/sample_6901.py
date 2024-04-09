offer_premise = float(input("Premise: Shop Offered less than 70% offer for every Shirt, Smith bought a shirt at Rs. "))
offer_hypothesis = float(input("Hypothesis: Shop Offered 30% offer for every Shirt, Smith bought a shirt at Rs. "))
shirt_price_premise = float(input("Premise: Smith bought a shirt at Rs. "))

# Check if the hypothesis value contradicts the premise value
if offer_hypothesis < offer_premise:
    label = "contradiction"
elif offer_hypothesis > offer_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
