percentage_increase_premise = 30
number_banks_premise = 90
number_banks_hypothesis = 117

# the hypothesis and premise mention the number of banks on the problem list and the percentage increase from the previous quarter
if number_banks_hypothesis!= number_banks_premise:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
elif percentage_increase_hypothesis > percentage_increase_premise:
    # check if the percentage increase in the hypothesis contradicts the premise estimate of 'percentage_increase_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage increase
    # any percentage increase in the hypothesis less than or equal to 'percentage_increase_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
