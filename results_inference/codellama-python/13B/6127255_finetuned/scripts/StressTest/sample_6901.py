shirt_discount_premise = 70
shirt_discount_hypothesis = 30

# the hypothesis talks about the discount percentage of a shirt, referenced also in the premise
if shirt_discount_hypothesis >= shirt_discount_premise:
    # check if the hypothesis value contradicts the estimate of less than'shirt_discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount percentage
    # any discount percentage less than'shirt_discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
