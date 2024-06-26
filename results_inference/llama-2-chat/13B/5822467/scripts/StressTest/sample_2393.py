# define variables with representative names for the numerical entities in both inputs
tshirts_premise = 8
tshirts_hypothesis = float(input("Enter the number of t-shirts bought by Sanoop: "))
average_price_premise = float(input("Enter the average price of the t-shirts (in Rs.): "))

# extract all quantities as valid numbers (integers or floats)
if tshirts_hypothesis < tshirts_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif average_price_premise!= average_price_hypothesis:
    # check if the estimate of 'average_price_hypothesis' contradicts the estimate of 'average_price_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
