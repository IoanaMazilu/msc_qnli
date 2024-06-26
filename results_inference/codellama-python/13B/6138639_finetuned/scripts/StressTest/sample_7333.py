samsung_premise = 25
samsung_hypothesis = 75
iphone_premise = 70
iphone_hypothesis = 70

# the hypothesis talks about the percentage of Samsung and i phone users in the same company, referenced also in the premise
if samsung_hypothesis <= samsung_premise:
    # check if the hypothesis value contradicts the estimate of more than'samsung_premise'
    label = "contradiction"
elif iphone_hypothesis!= iphone_premise:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of Samsung users
    # any percentage of Samsung users greater than'samsung_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
