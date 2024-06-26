# Define variables for the premise and hypothesis
premise_tshirts = float(input("Premise: Sanoop bought 8 t-shirts at an average price (arithmetic mean) of Rs."))
hypothesis_tshirts = float(input("Hypothesis: Sanoop bought more than 8 t-shirts at an average price (arithmetic mean) of Rs."))

# Check if the hypothesis value contradicts the premise value
if hypothesis_tshirts > premise_tshirts:
    label = "contradiction"
elif hypothesis_tshirts < premise_tshirts:
    label = "entailment"
else:
    label = "neutral"

print(label)
