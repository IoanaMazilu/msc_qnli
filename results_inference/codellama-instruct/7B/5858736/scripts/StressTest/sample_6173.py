# define variables for the numerical entities in the premise and hypothesis
tip_premise = 15
price_premise = 100
discount_premise = 20
tip_hypothesis = 25
price_hypothesis = 80
discount_hypothesis = 10

# calculate the total tip for John and Jane
tip_john = tip_premise/100*price_premise
tip_jane = tip_hypothesis/100*price_hypothesis

# calculate the total price for John and Jane
price_john = price_premise - discount_premise + tip_john
price_jane = price_hypothesis - discount_hypothesis + tip_jane

# compare the total prices for John and Jane
if price_john <= price_jane:
    # check if the estimate of 'price_john' contradicts the total price for John
    label = "contradiction"
elif price_jane!= price_john:
    # check if the total price for Jane contradicts the estimate of 'price_jane'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
