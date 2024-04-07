# Premise: The Computer Store has reduced the price of a computer by less than 55%. What is the original price of the computer if the sale price is $1275?
# Hypothesis: The Computer Store has reduced the price of a computer by 15%. What is the original price of the computer if the sale price is $1275?
# Golden Label: neutral

reduction_percentage_premise = 55
reduction_percentage_hypothesis = 15
sale_price_premise = 1275
sale_price_hypothesis = 1275

# the hypothesis refers to the reduction percentage and sale price mentioned in the premise
if reduction_percentage_hypothesis >= reduction_percentage_premise:
    # check if the 'reduction_percentage_hypothesis' contradicts the reduction percentage in the premise
    label = "contradiction"
elif sale_price_hypothesis != sale_price_premise:
    # check if the sale price in the hypothesis contradicts the sale price reported in the premise
    label = "contradiction"
else:
    # any reduction percentage less than 'reduction_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)

