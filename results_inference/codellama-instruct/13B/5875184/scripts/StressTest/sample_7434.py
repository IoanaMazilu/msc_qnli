premise_store_z = 90
premise_sales_tax = 0.2
premise_rebate = 10

hypothesis_store_z = 70
hypothesis_sales_tax = 0.2
hypothesis_rebate = 10

# calculate the total cost of the item in each scenario
premise_scenario_1 = premise_store_z * (1 - premise_sales_tax) + premise_rebate
premise_scenario_2 = premise_store_z * (1 - premise_sales_tax) + premise_rebate
premise_scenario_3 = premise_store_z * (1 - premise_sales_tax) + premise_rebate
premise_scenario_4 = premise_store_z * (1 - premise_sales_tax) + premise_rebate

hypothesis_scenario_1 = hypothesis_store_z * (1 - hypothesis_sales_tax) + hypothesis_rebate
hypothesis_scenario_2 = hypothesis_store_z * (1 - hypothesis_sales_tax) + hypothesis_rebate
hypothesis_scenario_3 = hypothesis_store_z * (1 - hypothesis_sales_tax) + hypothesis_rebate
hypothesis_scenario_4 = hypothesis_store_z * (1 - hypothesis_sales_tax) + hypothesis_rebate

# compare the total cost of the item in each scenario
if hypothesis_scenario_1 > premise_scenario_1:
    label = "entailment"
elif hypothesis_scenario_2 > premise_scenario_2:
    label = "entailment"
elif hypothesis_scenario_3 > premise_scenario_3:
    label = "entailment"
elif hypothesis_scenario_4 > premise_scenario_4:
    label = "entailment"
else:
    label = "neutral"

print(label)
