total_rainfall_premise = 25
total_rainfall_hypothesis = 65

# the hypothesis talks about the total rainfall in Springdale during the first two weeks of March, referenced also in the premise
if total_rainfall_hypothesis >= total_rainfall_premise:
    # check if the hypothesis value contradicts the estimate of less than 'total_rainfall_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total rainfall
    # any total rainfall less than 'total_rainfall_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
