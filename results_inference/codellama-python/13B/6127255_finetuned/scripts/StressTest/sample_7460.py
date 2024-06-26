min_lists_premise = 1/4
min_lists_hypothesis = 3/4
members_premise = 770
members_hypothesis = 770

# the hypothesis refers to the same criteria for considering a movie for the movie of the year as the premise
if min_lists_hypothesis < min_lists_premise or members_hypothesis!= members_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif min_lists_hypothesis == min_lists_premise and members_hypothesis == members_premise:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, but also cannot be fully entailed, we infer neutrality
    label = "neutral"

print(label)
