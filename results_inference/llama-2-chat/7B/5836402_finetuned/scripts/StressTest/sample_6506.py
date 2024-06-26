speed_premise = 40
speed_hypothesis = 10

# the hypothesis talks about the constant speed of Bob while driving from City A to City B, referenced also in the premise
if speed_hypothesis >= speed_premise:
    # check if the hypothesis value contradicts the premise value of'speed_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than'speed_premise', it is a valid estimate, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
