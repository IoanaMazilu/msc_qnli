# Define variables for the numerical entities in the premise and hypothesis
rupee_premise = 65.36
rupee_hypothesis = 68.19
sensex_premise = 300
sensex_hypothesis = 282.50
nifty_premise = 27
nifty_hypothesis = 28

# Extract all quantities as valid numbers
rupee_premise = float(rupee_premise)
rupee_hypothesis = float(rupee_hypothesis)
sensex_premise = float(sensex_premise)
sensex_hypothesis = float(sensex_hypothesis)
nifty_premise = float(nifty_premise)
nifty_hypothesis = float(nifty_hypothesis)

# Perform calculations if necessary
rupee_difference = rupee_hypothesis - rupee_premise
sensex_difference = sensex_hypothesis - sensex_premise
nifty_difference = nifty_hypothesis - nifty_premise

# Check for entailment, contradiction, or neutrality
if rupee_difference < 0:
    # The hypothesis is inconsistent with the premise
    label = "contradiction"
elif sensex_difference < 0:
    # The hypothesis is inconsistent with the premise
    label = "contradiction"
elif nifty_difference < 0:
    # The hypothesis is inconsistent with the premise
    label = "contradiction"
elif rupee_difference == 0 and sensex_difference == 0 and nifty_difference == 0:
    # The hypothesis is consistent with the premise
    label = "entailment"
else:
    # The hypothesis is neutral with respect to the premise
    label = "neutral"

print(label)
