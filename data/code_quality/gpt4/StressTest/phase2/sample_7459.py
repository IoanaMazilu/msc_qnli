lists_premise = 2/4
lists_hypothesis = 1/4
members_premise = 770
members_hypothesis = 770

# the hypothesis refers to the conditions for a movie to be considered as "movie of the year", stated also in the premise
if lists_premise < lists_hypothesis:
    # check if the hypothesis contradicts the premise by stating a higher minimum proportion of top-10-movies lists
    label = "contradiction"
elif members_hypothesis != members_premise:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
