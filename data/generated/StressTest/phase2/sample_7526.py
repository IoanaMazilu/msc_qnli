# Premise: How many different combinations of 4 passengers can be formed from John's 6 friends?
# Hypothesis: How many different combinations of more than 4 passengers can be formed from John's 6 friends?
# Golden Label: contradiction

passengers_premise = 4
passengers_hypothesis = 4
friends_premise = 6
friends_hypothesis = 6

# the hypothesis refers to the number of passengers that can be formed from the premise's number of John's friends
if passengers_hypothesis > passengers_premise:
    # check if 'passengers_hypothesis' contradicts the number of passengers in the premise
    label = "contradiction"
elif friends_hypothesis != friends_premise:
    # check if the number of friends in the hypothesis contradicts the number of friends mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, it is neutral
    label = "neutral"

print(label)

