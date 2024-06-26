# Define variables for the numerical entities in the premise and hypothesis
sensex_premise = 103
nifty_premise = 8900
stock_option_calls_premise = True

sensex_hypothesis = 100
nifty_hypothesis = 8900
stock_option_calls_hypothesis = True

# Extract all quantities as valid numbers
sensex_premise = int(sensex_premise)
nifty_premise = int(nifty_premise)
sensex_hypothesis = int(sensex_hypothesis)
nifty_hypothesis = int(nifty_hypothesis)

# Check if the hypothesis and premise have the same values
if sensex_premise == sensex_hypothesis and nifty_premise == nifty_hypothesis and stock_option_calls_premise == stock_option_calls_hypothesis:
    # The hypothesis and premise have the same values, so the hypothesis is entailed from the premise
    label = "entailment"
else:
    # The hypothesis and premise have different values, so the hypothesis is not entailed from the premise
    label = "contradiction"

print(label)
