passengers_premise = 4
friends_premise = 6
passengers_hypothesis = 4
friends_hypothesis = 6

# the hypothesis refers to the number of passengers and friends mentioned in the premise
if passengers_hypothesis >= passengers_premise and friends_hypothesis == friends_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif passengers_hypothesis < passengers_premise and friends_hypothesis == friends_premise:
    # check if the number of passengers in the hypothesis contradicts the number of passengers in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
