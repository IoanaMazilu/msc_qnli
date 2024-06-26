total_money_earned_premise = 9000
total_money_earned_hypothesis = 4000

if total_money_earned_hypothesis >= total_money_earned_premise:
    # check if the hypothesis value contradicts the total amount of money earned in the premise
    label = "contradiction"
else:
    # the premise gives a specific number for the total amount of money earned
    # any number of money less than 'total_money_earned_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
