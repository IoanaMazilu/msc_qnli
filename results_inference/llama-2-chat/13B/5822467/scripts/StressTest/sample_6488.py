rainfall_premise = 25
rainfall_hypothesis = float(input("Enter the total rainfall in Springdale during the first two weeks of March: "))

# check if the hypothesis value contradicts the premise value
if rainfall_hypothesis > rainfall_premise:
    label = "contradiction"
elif rainfall_hypothesis <= rainfall_premise:
    # check if the hypothesis value is consistent with the premise value
    label = "neutral"
else:
    # the premise gives only an estimate for the total rainfall
    # any value greater than 25 inches is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
