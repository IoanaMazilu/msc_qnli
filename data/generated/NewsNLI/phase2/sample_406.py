# Premise: Even so, the PGA Tour website noted that Woods moved up 20 spots in the Official World Golf Ranking with the win.
# Hypothesis: Woods jumps 20 spots in world golf rankings with the win, the PGA Tour says.
# Golden Label: entailment

spots_moved_up_premise = 20
spots_moved_up_hypothesis = 20

# the hypothesis mentions the number of spots Woods moved up in the world golf rankings, which is also mentioned in the premise
if spots_moved_up_hypothesis != spots_moved_up_premise:
    # check if the number of spots moved up in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the number of spots moved up in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

