total_matches_premise = 5
wins_premise = 21
losses_premise = 19
ties_premise = 104
total_games_premise = 144

# the hypothesis mentions Kasparov's victories in the rematch, but we cannot infer from the premise that this rematch is part of the total 5 world championship matches
# also, the specific victories in the first two games of the rematch are not mentioned in the premise
# hence, we cannot contradict or entail the hypothesis from the premise
label = "neutral"

print(label)
