# Premise: How many different combinations of 2 passengers can be formed from John's 4 friends?
# Hypothesis: How many different combinations of 5 passengers can be formed from John's 4 friends?
# Golden Label: contradiction

passengers_combinations_premise = 2
friends_premise = 4
passengers_combinations_hypothesis = 5
friends_hypothesis = 4

# the hypothesis refers to the number of passenger combinations and friends mentioned in the premise
if passengers_combinations_hypothesis > passengers_combinations_premise:
    # check if the number of 'passengers_combinations_hypothesis' contradicts the number of passenger combinations in the premise
    label = "contradiction"
elif friends_hypothesis != friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

