# Define variables for the premise and hypothesis
premise_gas_cans = 5.0
premise_gas_total = 20.0
hypothesis_gas_cans = 4.0

# Check if the number of gas cans in the hypothesis is less than or equal to the number of gas cans in the premise
if hypothesis_gas_cans <= premise_gas_cans:
    # Check if the total amount of gas in the hypothesis is greater than or equal to the total amount of gas in the premise
    if premise_gas_total / premise_gas_cans >= hypothesis_gas_cans * hypothesis_gas_cans:
        # If both conditions are true, we can infer entailment
        label = "entailment"
    else:
        # If the total amount of gas in the hypothesis is less than the total amount of gas in the premise, we can infer contradiction
        label = "contradiction"
else:
    # If the number of gas cans in the hypothesis is greater than the number of gas cans in the premise, we can infer contradiction
    label = "contradiction"

print(label)
