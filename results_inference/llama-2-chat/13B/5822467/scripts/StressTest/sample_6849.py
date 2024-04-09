billy_apples_premise = 10
billy_apples_hypothesis = 20

# the hypothesis refers to the number of apples Billy has, mentioned in the premise
if billy_apples_premise <= billy_apples_hypothesis:
    # check if the hypothesis value contradicts the estimate of less than 'billy_apples_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples Billy has
    # any number of apples less than 20 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
