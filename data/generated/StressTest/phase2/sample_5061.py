# Premise: A group of 5 friends — Archie, Betty, Jerry, Moose, and Veronica — arrived at the movie theater to see a movie.
# Hypothesis: A group of less than 8 friends — Archie, Betty, Jerry, Moose, and Veronica — arrived at the movie theater to see a movie.
# Golden Label: entailment

friends_premise = 5
friends_hypothesis = 8

# the hypothesis refers to the number of friends mentioned in the premise
if friends_hypothesis < friends_premise:
    # check if the hypothesis value contradicts the known number of friends from the premise
    label = "contradiction"
elif friends_hypothesis > friends_premise:
    # check if the hypothesis value is greater than the known number of friends from the premise
    # it doesn't contradict the premise, but it can’t be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"

print(label)

