watermelons_premise = 200
watermelons_hypothesis = 100

# the hypothesis talks about the number of watermelons Mike had, referenced also in the premise
if watermelons_hypothesis <= watermelons_premise:
    # check if the hypothesis value contradicts the number of watermelons in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of watermelons
    # any number of watermelons greater than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
