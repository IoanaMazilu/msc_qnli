rs_premise = 20
rs_hypothesis = float(input("Enter the price of Rs. for more than 20 each: "))

# check if the hypothesis value contradicts the premise value
if rs_hypothesis < rs_premise:
    label = "contradiction"
elif rs_hypothesis > rs_premise:
    # check if the hypothesis value entails the premise value
    if rs_hypothesis - rs_premise > 0:
        label = "entailment"
    else:
        label = "neutral"
else:
    label = "neutral"

print(label)
