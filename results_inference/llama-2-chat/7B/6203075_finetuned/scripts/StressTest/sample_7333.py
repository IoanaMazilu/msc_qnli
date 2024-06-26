samsung_percentage_premise = 25
samsung_percentage_hypothesis = 75
iphone_percentage_premise = 70
iphone_percentage_hypothesis = 70

# the hypothesis talks about the percentage of Samsung and iPhones in the same company,
# which is also mentioned in the premise
if samsung_percentage_hypothesis <= samsung_percentage_premise:
    # check if the hypothesis value contradicts the estimate of more than'samsung_percentage_premise'
    label = "contradiction"
elif iphone_percentage_hypothesis!= iphone_percentage_premise:
    # check if the percentage of iPhones in the hypothesis contradicts the percentage of iPhones reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of Samsung phones
    # any percentage greater than'samsung_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
