score_argentina_premise = 2
score_greece_premise = 0
score_south_korea_premise = 2
score_nigeria_premise = 0

score_south_korea_hypothesis = 2
score_nigeria_hypothesis = 2

# the hypothesis mentions the score of the match between South Korea and Nigeria, which is also referenced in the premise
# however, the hypothesis refers to South Korea as runners-up, which cannot be entailed from the premise
label = "neutral"

print(label)
