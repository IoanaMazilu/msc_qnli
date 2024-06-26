premise = "Norway's Current Account Surplus Adds US$4.61 Billion In Quarter 2 Of 2017 To The Economy."
hypothesis = "South Korea's Current Account Surplus Added USD 7.01 Billion In June Of 2017 To The Economy."

# define variables with representative names for the numerical entities in both inputs
surplus_premise = 4.61
surplus_hypothesis = 7.01

# extract all quantities as valid numbers (integers or floats)
if surplus_hypothesis > surplus_premise:
    # check if the hypothesis value is greater than the premise value
    label = "entailment"
elif surplus_hypothesis < surplus_premise:
    # check if the hypothesis value is less than the premise value
    label = "contradiction"
else:
    # check if the hypothesis value is equal to the premise value
    label = "neutral"

print(label)
