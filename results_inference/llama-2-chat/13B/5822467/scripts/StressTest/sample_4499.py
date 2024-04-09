cost_price = 100  # represent the cost price of the cupboard
discount_premise = 12  # represent the discount percentage in the premise
discount_hypothesis = 15  # represent the discount percentage in the hypothesis

# define variables with representative names for the numerical entities in both inputs
cupboard_sales_premise = cost_price * (1 - discount_premise / 100)
cupboard_sales_hypothesis = cost_price * (1 - discount_hypothesis / 100)

# extract all quantities as valid numbers (integers or floats)
cupboard_sales_premise = int(cupboard_sales_premise)
cupboard_sales_hypothesis = int(cupboard_sales_hypothesis)

# compare the variables
if cupboard_sales_hypothesis > cupboard_sales_premise:
    # the hypothesis refers to a higher discount than the premise, so we have entailment
    label = "entailment"
elif cupboard_sales_hypothesis == cupboard_sales_premise:
    # the hypothesis and premise have the same discount, so we have neutrality
    label = "neutral"
else:
    # the hypothesis refers to a lower discount than the premise, so we have contradiction
    label = "contradiction"

print(label)
