premise_unemployment_rate = 3.9
hypothesis_unemployment_rate = 3.9
premise_wage_growth = "weak"

# define variables with representative names for the numerical entities in both inputs
unemployment_rate_premise = premise_unemployment_rate
unemployment_rate_hypothesis = hypothesis_unemployment_rate
wage_growth_premise = premise_wage_growth

# extract all quantities as valid numbers (integers or floats)
unemployment_rate_premise = float(unemployment_rate_premise)
unemployment_rate_hypothesis = float(unemployment_rate_hypothesis)
wage_growth_premise = float(wage_growth_premise)

# compare the variables
if unemployment_rate_premise!= unemployment_rate_hypothesis:
    # check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
    label = "contradiction"
elif wage_growth_premise!= "weak" and wage_growth_hypothesis == "weak":
    # check if the estimated percentage of the total valuation in the hypothesis contradicts the premise estimate of more than 'percentage_of_valuation_premise'
    label = "neutral"
else:
    # the premise gives only an estimate for the percentage of the valuation
    # any estimate of the percentage in the hypothesis greater or equal to 'percentage_of_valuation_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
