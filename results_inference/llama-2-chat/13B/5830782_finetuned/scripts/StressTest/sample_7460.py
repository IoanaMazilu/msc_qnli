min_lists_premise = 1/4
min_lists_hypothesis = 3/4
members_premise = 770
members_hypothesis = 770

# the hypothesis refers to the same requirements for a movie to be considered for the movie of the year
# but changes the minimum number of lists and members from the premise
if min_lists_premise!= min_lists_hypothesis:
    # check if the minimum number of lists in the hypothesis contradicts the minimum number of lists in the premise
    label = "contradiction"
elif members_premise!= members_hypothesis:
    # check if the number of members in the hypothesis contradicts the number of members in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
