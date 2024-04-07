# Premise: Patrick has a locker with a less than 8 number combination.
# Hypothesis: Patrick has a locker with a 3 number combination.
# Golden Label: neutral

locker_combination_premise = 8
locker_combination_hypothesis = 3

# the hypothesis refers to the number of combinations of Patrick's locker, also mentioned in the premise
if locker_combination_hypothesis >= locker_combination_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'locker_combination_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the number of locker combinations
    # any number of combinations less than 'locker_combination_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

