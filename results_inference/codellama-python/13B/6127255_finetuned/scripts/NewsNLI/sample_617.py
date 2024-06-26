norwich_score_premise = 1
united_score_premise = 0
manchester_city_score_premise = 5
norwich_score_hypothesis = 1
united_score_hypothesis = 0

# the hypothesis mentions the score of the game between Norwich and United, which is also mentioned in the premise
# however, the hypothesis refers to Manchester United, which cannot be entailed from the premise
label = "neutral"

print(label)
