n_premise = 6 # number of boxes in the premise
mark_sold_premise = n_premise - 6 # number of boxes sold by Mark in the premise
ann_sold_premise = n_premise - 2 # number of boxes sold by Ann in the premise

# define variables for the hypothesis
mark_sold_hypothesis = n_premise - 1 # number of boxes sold by Mark in the hypothesis
ann_sold_hypothesis = n_premise - 2 # number of boxes sold by Ann in the hypothesis

# check if the hypothesis values contradict the premise values
if mark_sold_hypothesis < mark_sold_premise:
    # Mark sold fewer boxes in the hypothesis than in the premise, so no contradiction
    label = "neutral"
elif ann_sold_hypothesis < ann_sold_premise:
    # Ann sold fewer boxes in the hypothesis than in the premise, so no contradiction
    label = "neutral"
else:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"

print(label)
