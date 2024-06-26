square_feet_premise = 800
square_feet_hypothesis = 900
price_premise = 1500
price_hypothesis = 1500

# the hypothesis talks about the size of the property and its price, referenced also in the premise
if square_feet_hypothesis!= square_feet_premise:
    # check if the estimate of'square_feet_hypothesis' contradicts the size of the property in the premise
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the price of the property in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
