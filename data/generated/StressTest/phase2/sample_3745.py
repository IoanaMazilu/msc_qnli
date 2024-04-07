# Premise: Bhajan Singh purchased less than 220 reams of paper at Rs 80 per ream.
# Hypothesis: Bhajan Singh purchased 120 reams of paper at Rs 80 per ream.
# Golden Label: neutral

paper_reams_premise = 220
paper_reams_hypothesis = 120

# the hypothesis talks about the number of reams purchased, which is also referenced in the premise
if paper_reams_hypothesis >= paper_reams_premise:
    # check if the number of paper reams in the hypothesis contradicts the estimate of less than 'paper_reams_premise' 
    label = "contradiction"
elif paper_reams_hypothesis < paper_reams_premise:
    # the premise provides an estimate for the number of paper reams
    # any number of paper reams less than 'paper_reams_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

