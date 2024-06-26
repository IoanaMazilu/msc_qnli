min_lists_premise = 2/4
min_lists_hypothesis = 1/4
members_premise = 770
members_hypothesis = 770

# the hypothesis refers to the same criteria for considering a movie for the movie of the year as the premise
if min_lists_hypothesis >= min_lists_premise:
    # check if the hypothesis value contradicts the estimate of less than'min_lists_premise'
    label = "contradiction"
elif members_hypothesis!= members_premise:
    # check if the number of members in the hypothesis contradicts the number of members reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the minimum lists
    # any number of lists less than'min_lists_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
