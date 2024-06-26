premise_shirts = 80
hypothesis_shirts = 40

# the hypothesis refers to the number of shirts each person has, which is not explicitly mentioned in the premise
if hypothesis_shirts <= premise_shirts:
    # check if the hypothesis value contradicts the estimate of less than 'premise_shirts'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts greater than 'premise_shirts' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
