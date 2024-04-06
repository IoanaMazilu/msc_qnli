# Premise: Despite Wood's determined effort, Warrington lost the match 26-18 to 2011 champions Leeds.
# Hypothesis: Warrington lost the match at Old Trafford 26-18.
# Golden Label: neutral

score_premise = [26, 18]
score_hypothesis = [26, 18]

# the hypothesis mentions the score of the match, which is also mentioned in the premise
# however, the hypothesis refers to the location of the match, which cannot be entailed from the premise
if score_hypothesis != score_premise:
    # check if the score in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
else:
    # if the score from the hypothesis does not contradict the score in the premise, we can infer neutrality
    label = "neutral"

print(label)

