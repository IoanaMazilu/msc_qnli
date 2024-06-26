premise = "If gas costs $more than 2/gallon, then how many miles can Dan’s car go on $42 of gas?"
hypothesis = "If gas costs $4/gallon, then how many miles can Dan’s car go on $42 of gas?"

# extract the numerical entities from the premise and hypothesis
premise_gas_cost = float(premise.split("$")[1].split("/")[0])
hypothesis_gas_cost = float(hypothesis.split("$")[1].split("/")[0])
premise_miles = float(premise.split("miles")[0].split("can")[1].split("go")[1].split("on")[1].split("$")[0])
hypothesis_miles = float(hypothesis.split("miles")[0].split("can")[1].split("go")[1].split("on")[1].split("$")[0])

# perform the calculations
premise_gas_cost_per_mile = premise_gas_cost / premise_miles
hypothesis_gas_cost_per_mile = hypothesis_gas_cost / hypothesis_miles

# compare the gas cost per mile
if hypothesis_gas_cost_per_mile < premise_gas_cost_per_mile:
    label = "entailment"
elif hypothesis_gas_cost_per_mile > premise_gas_cost_per_mile:
    label = "contradiction"
else:
    label = "neutral"

print(label)
