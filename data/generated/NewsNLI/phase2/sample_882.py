# Premise: Earlier, England had lost their last six wickets for just 17 runs as Mohammad Asif took five wickets for Pakistan.
# Hypothesis: James Anderson takes five wickets as Pakistan collapse against England.
# Golden Label: neutral

wickets_lost_premise = 6
runs_premise = 17
wickets_taken_premise = 5

wickets_taken_hypothesis = 5

# the hypothesis mentions the number of wickets taken, which is also referenced in the premise
# however, the hypothesis refers to a different player and team, which cannot be entailed from the premise
label = "neutral"

print(label)

