# Define variables for the numerical entities in the premise and hypothesis
premise_share_Deepak = 4300
hypothesis_share_Deepak = 1300

# Extract all quantities as valid numbers
premise_share_Deepak = int(premise_share_Deepak)
hypothesis_share_Deepak = int(hypothesis_share_Deepak)

# Use brief comments to explain what comparison you do between the defined variables
if hypothesis_share_Deepak <= premise_share_Deepak:
    # Check if the hypothesis value contradicts the estimate of less than 'premise_share_Deepak'
    label = "contradiction"
else:
    # The premise gives only an estimate for the share of Deepak
    # Any number of shares greater than 'premise_share_Deepak' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
