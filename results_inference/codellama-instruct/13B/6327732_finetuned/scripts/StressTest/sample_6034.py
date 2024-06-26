premise_owners = 70
hypothesis_owners = 40

# the hypothesis refers to the number of people owning cats, dogs, or rabbits in the city of San Durango
if hypothesis_owners >= premise_owners:
    # check if the hypothesis value contradicts the estimate of less than 'premise_owners'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people owning cats, dogs, or rabbits
    # any number of people owning cats, dogs, or rabbits less than 'premise_owners' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
