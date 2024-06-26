# Define variables for the numerical entities in the premise and hypothesis
premise_sensex_close = 362.75
premise_nifty_close = 0

hypothesis_sensex_close = 357.39
hypothesis_nifty_close = 0

# Extract all quantities as valid numbers
premise_sensex_close = float(premise_sensex_close)
premise_nifty_close = float(premise_nifty_close)

hypothesis_sensex_close = float(hypothesis_sensex_close)
hypothesis_nifty_close = float(hypothesis_nifty_close)

# Check if the premise and hypothesis have the same number of points
if premise_sensex_close!= hypothesis_sensex_close:
    # The hypothesis and premise have different number of points, so the hypothesis cannot be entailed from the premise
    label = "contradiction"
else:
    # The premise and hypothesis have the same number of points, so the hypothesis can be entailed from the premise
    label = "entailment"

print(label)
