number_banks_premise = 90
number_banks_hypothesis = 117
percentage_increase_premise = 30

# the hypothesis and premise mention the number of banks on the problem list and the percentage increase in the second quarter
if number_banks_premise!= number_banks_hypothesis:
    # check if the number of banks in the hypothesis contradicts the number of banks in the premise
    label = "contradiction"
elif percentage_increase_hypothesis < percentage_increase_premise:
    # check if the estimated percentage increase in the hypothesis contradicts the premise estimate of 30%
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage increase
    # any estimate of the percentage increase in the hypothesis greater or equal to 30% is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
