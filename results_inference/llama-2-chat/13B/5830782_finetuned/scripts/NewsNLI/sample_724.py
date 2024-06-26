argentina_score_premise = 2
greece_score_premise = 0
south_korea_score_premise = 2
nigeria_score_premise = 2

south_korea_score_hypothesis = 2
nigeria_score_hypothesis = 2

# the hypothesis mentions South Korea's score and Nigeria's score, which are also mentioned in the premise
# however, the hypothesis refers to South Korea as the runners-up, which cannot be entailed from the premise
label = "neutral"

print(label)
