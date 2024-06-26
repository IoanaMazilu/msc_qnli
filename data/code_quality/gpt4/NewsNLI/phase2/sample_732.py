snow_inches_premise = 32
snow_feet_hypothesis = 3.5

# 3.5 feet is approximately 42 inches
snow_inches_hypothesis = snow_feet_hypothesis * 12

# the hypothesis mentions a snow forecast, which is more than the snow received mentioned in the premise
if snow_inches_hypothesis <= snow_inches_premise:
    # check if the snow forecast in the hypothesis contradicts the snow received reported in the premise
    label = "contradiction"
else:
    # if the forecast does not contradict the snow received, we infer a neutral relation as we can't explicitly entail the forecast from the received snow
    label = "neutral"

print(label)
