more_supermarkets_US_premise = 60
more_supermarkets_US_hypothesis = 10

# the hypothesis refers to the number of FGH supermarkets in the US more than in Canada mentioned in the premise
if more_supermarkets_US_hypothesis >= more_supermarkets_US_premise:
    # check if the estimate of 'more_supermarkets_US_hypothesis' contradicts the number of FGH supermarkets in the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the FGH supermarkets more in the US than in Canada
    # any number of FGH supermarkets less than 'more_supermarkets_US_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
