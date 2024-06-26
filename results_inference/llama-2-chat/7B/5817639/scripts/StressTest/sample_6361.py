watermelons_premise = 700
watermelons_hypothesis = 200

# the hypothesis talks about the number of watermelons, referenced also in the premise
if watermelons_hypothesis <= watermelons_premise:
    # check if the hypothesis value contradicts the estimate of less than 'watermelons_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of watermelons
    # any number of watermelons greater than 'watermelons_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
