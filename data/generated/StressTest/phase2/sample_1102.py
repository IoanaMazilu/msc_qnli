# Premise: How many different combinations of more than 1 passengers can be formed from John's 6 friends?
# Hypothesis: How many different combinations of 2 passengers can be formed from John's 6 friends?
# Golden Label: neutral

combinations_premise_min = 2
friends_premise = 6
combinations_hypothesis = 2
friends_hypothesis = 6

# the hypothesis refers to the number of combinations that can be formed from John's friends, which is also mentioned in the premise
if combinations_hypothesis < combinations_premise_min:
    # check if the number of combinations in the hypothesis contradicts the minimum number of combinations in the premise
    label = "contradiction"
elif friends_hypothesis != friends_premise:
    # check if the number of John's friends in the hypothesis contradicts the number of John's friends in the premise
    label = "contradiction"
elif combinations_hypothesis > combinations_premise_min:
    # the premise only allows for combinations of more than one friend, any specific number greater than one cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

