# Premise: Carina has less than 230 ounces of coffee divided into 5-and 10-ounce packages.
# Hypothesis: Carina has 130 ounces of coffee divided into 5-and 10-ounce packages.
# Golden Label: neutral

coffee_premise = 230
coffee_hypothesis = 130

# the hypothesis talks about the quantity of coffee Carina has, referenced also in the premise
if coffee_hypothesis >= coffee_premise:
    # check if the quantity in the hypothesis contradicts the premise of having less than 'coffee_premise'
    label = "contradiction"
elif coffee_hypothesis < coffee_premise:
    # if the quantity in the hypothesis is less than 'coffee_premise', it does not contradict the premise
    # however, the exact quantity cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

