# Define variables for the premise and hypothesis
tax_cut_premise = 300
tax_cut_hypothesis = 300

# Check if the number of tax cuts in the hypothesis contradicts the premise
if tax_cut_hypothesis!= tax_cut_premise:
    label = "contradiction"
else:
    # If the number of tax cuts in the hypothesis is the same as in the premise, check if the estimated value of the tax cuts in the hypothesis contradicts the premise
    if tax_cut_hypothesis > tax_cut_premise:
        label = "contradiction"
    else:
        # If the estimated value of the tax cuts in the hypothesis is less than or equal to the premise, the hypothesis is neutral
        label = "neutral"

print(label)
