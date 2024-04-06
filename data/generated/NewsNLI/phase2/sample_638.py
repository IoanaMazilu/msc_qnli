# Premise: By the close of play Pakistan had reached 42-0, trailing their opponents by just 150 runs.
# Hypothesis: Pakistan reach 42-0 at the close of play to take charge of the match.
# Golden Label: neutral

score_pakistan_premise = 42
score_pakistan_hypothesis = 42
trailing_runs_premise = 150

# the hypothesis mentions the score of Pakistan, which is also mentioned in the premise
# however, the hypothesis infers Pakistan is in charge of the match, which cannot be entailed from the premise
label = "neutral"

print(label)

