price_premise = 1000
price_hypothesis = 1000
sqft_premise = 800
sqft_hypothesis = 700

# the hypothesis talks about the price of a property and its size, both referenced in the premise
if price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
elif sqft_hypothesis >= sqft_premise:
    # check if the size of the property in the hypothesis contradicts the estimate of less than'sqft_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the property
    # any size less than'sqft_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
