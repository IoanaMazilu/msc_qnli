microtron_premise = 76
dynaco_premise = 68
shares_premise = 300
average_price_premise = 40

microtron_hypothesis = 36
dynaco_hypothesis = 68

# define variables with representative names for the numerical entities in both inputs
microtron_sales = microtron_premise * shares_premise
dynaco_sales = dynaco_premise * shares_premise

# extract all quantities as valid numbers (integers or floats)
microtron_sales = int(microtron_sales)
dynaco_sales = int(dynaco_sales)

# compare the defined variables
if microtron_sales > dynaco_sales:
    # the hypothesis refers to the number of sold MicroTron stock, which is greater than the number of sold Dynaco stock
    label = "entailment"
elif microtron_sales == dynaco_sales:
    # the number of sold MicroTron stock and Dynaco stock are the same
    label = "neutral"
else:
    # the number of sold MicroTron stock is less than the number of sold Dynaco stock, which contradicts the premise
    label = "contradiction"

print(label)
