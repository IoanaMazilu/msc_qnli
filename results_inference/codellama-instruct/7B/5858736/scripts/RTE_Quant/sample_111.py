# Define variables for the numerical entities in the premise and hypothesis
premise_sale_price = 27.5e9
premise_company_price = 9.4e9
premise_company_name = "Yukos"
premise_buyer_name = "Baikalfinansgroup"
premise_buyer_state = "little known"
premise_buyer_country = "Russia"
premise_buyer_company = "Rosneft"

hypothesis_company_price = 27.5e9

# Extract all quantities as valid numbers
premise_sale_price = float(premise_sale_price)
premise_company_price = float(premise_company_price)
hypothesis_company_price = float(hypothesis_company_price)

# Use brief comments to explain what comparison you do between the defined variables
if premise_company_price!= hypothesis_company_price:
    # Check if the price of the company in the premise and hypothesis are different
    label = "contradiction"
else:
    # If the price of the company in the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)
