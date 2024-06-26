ram_krish_premise = 20
ram_krish_hypothesis = 40

# the hypothesis refers to the number of days Ram and Krish can complete a work, also mentioned in the premise
if ram_krish_hypothesis <= ram_krish_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ram_krish_premise' days
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'ram_krish_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
