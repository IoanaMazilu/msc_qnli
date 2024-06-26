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
