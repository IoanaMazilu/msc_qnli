# Premise: While Kiran playing all but 3 got destroyed.
# Hypothesis: While Kiran playing all but less than 8 got destroyed.
# Golden Label: entailment

destroyed_premise = 3
destroyed_hypothesis = 8

# the hypothesis talks about the number of destroyed items while Kiran was playing, referenced also in the premise
if destroyed_hypothesis <= destroyed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'destroyed_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of destroyed items
    # any number of destroyed items greater than 'destroyed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

