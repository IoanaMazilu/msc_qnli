# Premise: To be considered for “ movie of the year, ” a film must appear in at least 1/4 of the top-10-movies lists submitted by the Cinematic Academy’s 785 members.
# Hypothesis: To be considered for “ movie of the year, ” a film must appear in at least less than 6/4 of the top-10-movies lists submitted by the Cinematic Academy’s 785 members.
# Golden Label: entailment

movie_lists_premise = 1/4
movie_lists_hypothesis = 6/4
members_premise = 785
members_hypothesis = 785

# the hypothesis refers to the same condition for a movie to be considered for "movie of the year", as mentioned in the premise
if members_hypothesis != members_premise:
    # check if the number of members in the hypothesis contradicts the number of members stated in the premise
    label = "contradiction"
elif movie_lists_hypothesis <= movie_lists_premise:
    # check if the hypothesis value contradicts the condition in the premise
    label = "contradiction"
else:
    # the premise gives a condition for a movie to be considered for "movie of the year"
    # any condition more than 'movie_lists_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

