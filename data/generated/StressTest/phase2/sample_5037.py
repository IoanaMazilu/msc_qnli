# Premise: How many different combinations of 3 passengers can be formed from John's 6 friends?
# Hypothesis: How many different combinations of less than 8 passengers can be formed from John's 6 friends?
# Golden Label: entailment

passenger_combinations_premise = 3
passenger_combinations_hypothesis = 8
total_friends = 6

# the hypothesis refers to the number of passenger combinations from John's friends mentioned in the premise
if passenger_combinations_hypothesis <= passenger_combinations_premise:
    # check if the number of 'passenger_combinations_hypothesis' contradicts the number of passenger combinations in the premise
    label = "contradiction"
elif passenger_combinations_hypothesis > total_friends:
    # check if the number of 'passenger_combinations_hypothesis' contradicts the total number of John's friends
    label = "contradiction"
else:
    # any number of passenger combinations less than 'passenger_combinations_hypothesis' and less than or equal to 'total_friends' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

