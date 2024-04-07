# Premise: more than 4887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Hypothesis: 5887 is divided between Shyam and Ram, such that Shyam's share at the end of 9 years is equal to Ram's share at the end of 11 years, compounded annually at the rate of 5 %.
# Golden Label: neutral

total_money_premise = 4887
total_money_hypothesis = 5887

# the hypothesis specifies a total amount of money divided between Shyam and Ram referenced in the premise
if total_money_hypothesis <= total_money_premise:
    # check if the total amount of money in the hypothesis contradicts the estimate of more than 'total_money_premise'
    label = "contradiction"
else:
    # the premise only gives an estimate for the total amount of money
    # any total amount of money greater than 'total_money_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

