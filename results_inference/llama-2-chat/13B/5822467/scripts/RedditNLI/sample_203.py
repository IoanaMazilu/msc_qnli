premise = "The 2005 Bankruptcy Reform and the Foreclosure Crisis."
hypothesis = "Insolvency after the 2005 Bankruptcy Reform."

# define variables with representative names for the numerical entities in both inputs
reform_year = 2005
crisis_year = 2005

# extract all quantities as valid numbers (integers or floats)
reform_year_int = int(reform_year)
crisis_year_int = int(crisis_year)

# compare the variables
if reform_year_int!= crisis_year_int:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
elif crisis_year_int < reform_year_int:
    # check if the year of the crisis in the premise is before the year of the reform in the hypothesis
    label = "contradiction"
else:
    # the premise and hypothesis mention the same year for the reform and the crisis, so there is no contradiction
    label = "neutral"

print(label)
