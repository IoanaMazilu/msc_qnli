# Premise: Celtic went into the match in the Russian capital with a record of 11 straight losses on the road in the Champions League and 21 games without a win away from home.
# Hypothesis: Celtic snap away drought with superb 3-2 win in Moscow.
# Golden Label: neutral

straight_losses_premise = 11
games_without_win_premise = 21
win_hypothesis = 1

# the hypothesis mentions a win for Celtic, which contradicts the premise
if win_hypothesis > 0:
    label = "contradiction"

print(label)

