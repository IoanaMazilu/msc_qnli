# Define variables with representative names for the numerical entities in both inputs
cookies_eaten_michael = 1/8
cookies_eaten_steve = 1/2
cookies_eaten_tyler = 150

# Extract all quantities as valid numbers (integers or floats)
cookies_eaten_michael = float(cookies_eaten_michael)
cookies_eaten_steve = float(cookies_eaten_steve)
cookies_eaten_tyler = float(cookies_eaten_tyler)

# Use brief comments to explain what comparison you do between the defined variables
if cookies_eaten_michael <= cookies_eaten_steve:
    # Check if the estimate of 'cookies_eaten_steve' contradicts the number of cookies eaten by Michael
    label = "contradiction"
elif cookies_eaten_tyler <= cookies_eaten_michael:
    # Check if the estimate of 'cookies_eaten_tyler' contradicts the number of cookies eaten by Michael
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
