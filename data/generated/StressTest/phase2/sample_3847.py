# Premise: If Grady and Howard are among those more than 5 friends but can never sit next to each other, how many 6-person seating arrangements are possible?
# Hypothesis: If Grady and Howard are among those 6 friends but can never sit next to each other, how many 6-person seating arrangements are possible?
# Golden Label: neutral

friends_premise = 5
friends_hypothesis = 6

# the hypothesis refers to the number of friends mentioned in the premise
if friends_premise != friends_hypothesis:
    # check if the number of friends in the hypothesis contradicts the number of friends mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

