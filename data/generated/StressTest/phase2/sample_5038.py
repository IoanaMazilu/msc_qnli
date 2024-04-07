# Premise: How many different combinations of less than 8 passengers can be formed from John's 6 friends?
# Hypothesis: How many different combinations of 3 passengers can be formed from John's 6 friends?
# Golden Label: neutral

combinations_premise = 8
combinations_hypothesis = 3

# the hypothesis refers to the number of possible combinations from John's friends mentioned in the premise
if combinations_hypothesis >= combinations_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'combinations_premise'
    label = "contradiction"
elif combinations_hypothesis < combinations_premise:
    # the premise gives an estimate for the maximum number of combinations
    # any number of combinations less than 'combinations_premise' can be explicitly entailed from the premise
    label = "entailment"

print(label)

