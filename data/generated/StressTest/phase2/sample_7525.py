# Premise: How many different combinations of more than 2 passengers can be formed from John's 6 friends?
# Hypothesis: How many different combinations of 4 passengers can be formed from John's 6 friends?
# Golden Label: neutral

passenger_combinations_premise = 2
passenger_combinations_hypothesis = 4
friends_premise = 6
friends_hypothesis = 6

# The hypothesis refers to the number of passenger combinations and friends, also mentioned in the premise
if passenger_combinations_hypothesis <= passenger_combinations_premise:
    # Check if the number of passenger combinations in the hypothesis contradicts the premise's estimate of more than 'passenger_combinations_premise'
    label = "contradiction"
elif friends_hypothesis != friends_premise:
    # Check if the number of friends in the hypothesis contradicts the number of friends in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of passenger combinations
    # Any number of combinations greater than 'passenger_combinations_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

