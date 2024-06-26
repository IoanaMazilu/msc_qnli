min_lists_premise = 1/4
min_lists_hypothesis = 2/4
members_premise = 770
members_hypothesis = 770

# the hypothesis refers to the same criteria for considering a movie for the movie of the year as the premise
if min_lists_hypothesis <= min_lists_premise or members_hypothesis!= members_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
