# Premise: What is the ratio of Arun's monthly income in the year 2006, Suman's monthly income in the year 2007 and Jyothi's monthly income in the year 2005?
# Hypothesis: What is the ratio of Arun's monthly income in the year more than 2006, Suman's monthly income in the year 2007 and Jyothi's monthly income in the year 2005?
# Golden Label: contradiction

arun_income_year_premise = 2006
arun_income_year_hypothesis = 2006
suman_income_year_premise = 2007
suman_income_year_hypothesis = 2007
jyothi_income_year_premise = 2005
jyothi_income_year_hypothesis = 2005

# the hypothesis refers to the years of income for the same people mentioned in the premise
if arun_income_year_hypothesis <= arun_income_year_premise:
    # check if the year of Arun's income in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
elif suman_income_year_hypothesis != suman_income_year_premise or jyothi_income_year_hypothesis != jyothi_income_year_premise:
    # check if the year of Suman's or Jyothi's income in the hypothesis contradicts the year mentioned in the premise
    label = "contradiction"
else:
    # if the years in the hypothesis do not contradict the years in the premise, we can infer entailment
    label = "entailment"

print(label)

