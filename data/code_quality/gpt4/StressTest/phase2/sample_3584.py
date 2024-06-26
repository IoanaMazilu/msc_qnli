more_supermarkets_us_premise = 14
more_supermarkets_us_hypothesis = 14

# the hypothesis talks about the number of FGH supermarkets in the US, referenced also in the premise
if more_supermarkets_us_hypothesis >= more_supermarkets_us_premise:
    # check if the hypothesis value contradicts the estimate of more than 'more_supermarkets_us_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of FGH supermarkets in the US
    # any number of supermarkets less than 'more_supermarkets_us_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
