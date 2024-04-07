# Premise: A group of less than 8 friends — Archie, Betty, Jerry, Moose, and Veronica — arrived at the movie theater to see a movie.
# Hypothesis: A group of 5 friends — Archie, Betty, Jerry, Moose, and Veronica — arrived at the movie theater to see a movie.
# Golden Label: neutral

friends_premise = 8
friends_hypothesis = 5

# the hypothesis refers to the group of friends mentioned in the premise
if friends_hypothesis >= friends_premise:
    # check if the number of friends in the hypothesis contradicts the premise statement of less than 'friends_premise'
    label = "contradiction"
else:
    # the premise gives only an upper limit for the number of friends
    # any number of friends less than 'friends_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

