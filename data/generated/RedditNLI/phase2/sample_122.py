# Premise: No, GDP isn't exceeding unemployment for the first time in 100 years.
# Hypothesis: GDP Growth Eclipses Unemployment For 1st Time In 100 Years.
# Golden Label: contradiction

years_premise = 100
years_hypothesis = 100

# the hypothesis and premise mention the number of years since GDP exceeded unemployment
if years_hypothesis != years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # the premise clearly states that GDP is not exceeding unemployment for the first time in 100 years
    # while the hypothesis states the contrary
    label = "contradiction"

print(label)

