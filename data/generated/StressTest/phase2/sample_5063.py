# Premise: A group of 5 friends — Archie, Betty, Jerry, Moose, and Veronica — arrived at the movie theater to see a movie.
# Hypothesis: A group of less than 5 friends — Archie, Betty, Jerry, Moose, and Veronica — arrived at the movie theater to see a movie.
# Golden Label: contradiction

friends_premise = 5
friends_hypothesis = 5

# the hypothesis refers to the number of friends mentioned in the premise
if friends_hypothesis >= friends_premise:
    # check if the hypothesis value contradicts the estimate of less than 'friends_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number of friends
    # any number of friends less than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

