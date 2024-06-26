# Variables for premise and hypothesis
premise_shares_MicroTron = 300
premise_shares_Dynaco = 300
hypothesis_shares_MicroTron = 76
hypothesis_shares_Dynaco = 48

# Calculate the average price per share for both stocks
average_price_MicroTron = (premise_shares_MicroTron * 36) / premise_shares_MicroTron
average_price_Dynaco = (premise_shares_Dynaco * 48) / premise_shares_Dynaco

# Check if the hypothesis value contradicts the premise value
if hypothesis_shares_MicroTron > premise_shares_MicroTron:
    label = "contradiction"
elif hypothesis_shares_Dynaco < premise_shares_Dynaco:
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
