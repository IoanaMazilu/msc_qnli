argentina_score_premise = 2
greece_score_premise = 0
south_korea_score_premise = 2
nigeria_score_premise = 2

south_korea_score_hypothesis = 2
nigeria_score_hypothesis = 2

# the hypothesis mentions the score of the South Korea vs Nigeria match, which is also mentioned in the premise
# however, the hypothesis infers that South Korea qualified as runners-up, which cannot be entailed from the premise
label = "neutral"

print(label)
