arun_income_year_premise = 2006
arun_income_year_hypothesis = 6006
suman_income_year_premise = 2007
suman_income_year_hypothesis = 2007
jyothi_income_year_premise = 2005
jyothi_income_year_hypothesis = 2005

# the hypothesis refers to the years of income for Arun, Suman, and Jyothi mentioned in the premise
if arun_income_year_hypothesis != arun_income_year_premise and arun_income_year_hypothesis > arun_income_year_premise:
    # check if the year of income for Arun in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif suman_income_year_hypothesis != suman_income_year_premise:
    # check if the year of income for Suman in the hypothesis contradicts the year in the premise
    label = "contradiction"
elif jyothi_income_year_hypothesis != jyothi_income_year_premise:
    # check if the year of income for Jyothi in the hypothesis contradicts the year in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
