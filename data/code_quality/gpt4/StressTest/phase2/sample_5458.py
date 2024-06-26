arun_income_year_premise = 6006
arun_income_year_hypothesis = 2006
suman_income_year_premise = 2007
suman_income_year_hypothesis = 2007
jyothi_income_year_premise = 2005
jyothi_income_year_hypothesis = 2005

# the hypothesis talks about the same incomes and years for Suman and Jyothi as in the premise
# but for Arun's income, the years in the premise and hypothesis are different
if arun_income_year_hypothesis >= arun_income_year_premise:
    # check if the year in the hypothesis contradicts the premise that the year is less than 'arun_income_year_premise'
    label = "contradiction"
elif suman_income_year_hypothesis != suman_income_year_premise or jyothi_income_year_hypothesis != jyothi_income_year_premise:
    # check if the years for Suman and Jyothi in the hypothesis contradict the years in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the year of Arun's income
    # any year less than 'arun_income_year_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
