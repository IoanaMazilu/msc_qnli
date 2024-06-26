straight_losses_premise = 11
games_without_win_premise = 21
win_hypothesis = 1

# the hypothesis mentions a win for Celtic, which contradicts the premise
if win_hypothesis > 0:
    label = "contradiction"

print(label)
