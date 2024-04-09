premise = "U.S. economy off to slow start in 2017 under Trump."
hypothesis = "GDP Report Shows US Economy Off to Slow Start in 2017."

# define variables with representative names for the numerical entities in both inputs
gdp_premise = float(premise.split()[1])
gdp_hypothesis = float(hypothesis.split()[1])

# extract all quantities as valid numbers (integers or floats)
gdp_premise_quant = float(gdp_premise.split()[0])
gdp_hypothesis_quant = float(gdp_hypothesis.split()[0])

# compare the variables
if gdp_hypothesis_quant!= gdp_premise_quant:
    # check if the numerical value in the hypothesis contradicts the premise
    label = "contradiction"
elif gdp_hypothesis_quant < gdp_premise_quant:
    # check if the numerical value in the hypothesis is less than the premise
    label = "entailment"
else:
    # the hypothesis and premise mention the same numerical value, so the comparison is neutral
    label = "neutral"

print(label)
