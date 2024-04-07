# Premise: How many different combinations of 4 passengers can be formed from John's 6 friends?
# Hypothesis: How many different combinations of more than 2 passengers can be formed from John's 6 friends?
# Golden Label: entailment

passengers_combinations_premise = 4
passengers_combinations_hypothesis = 2
total_friends = 6

# the hypothesis refers to the number of passenger combinations mentioned in the premise
if passengers_combinations_hypothesis >= passengers_combinations_premise:
    # check if the estimate of 'passengers_combinations_hypothesis' contradicts the number of passenger combinations in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of passenger combinations
    # any number of passenger combinations less than 'passengers_combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

