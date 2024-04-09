efficient_manufacturing_premise = 60
efficient_manufacturing_hypothesis = 30

# the hypothesis talks about the number of electronics components that a factory must manufacture, referenced also in the premise
if efficient_manufacturing_hypothesis <= efficient_manufacturing_premise:
    # check if the hypothesis value contradicts the estimate of more than 'efficient_manufacturing_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of electronics components
    # any number of electronics components greater than 'efficient_manufacturing_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
