# Premise: Hong Kong Raises Base Rate for First Time Since 2006 After Fed.
# Hypothesis: Mexico Raises Key Rate for First Time Since 2008 After Fed.
# Golden Label: neutral

year_premise = 2006
country_premise = "Hong Kong"
year_hypothesis = 2008
country_hypothesis = "Mexico"

# the hypothesis and premise are about different countries raising their base rates for the first time since a certain year after the Fed
# check if the countries and years in the hypothesis and premise are different
if country_premise != country_hypothesis or year_premise != year_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)

