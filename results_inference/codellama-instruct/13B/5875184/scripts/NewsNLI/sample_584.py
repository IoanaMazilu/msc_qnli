premise_score = 7-6(5) 6-7(4) 6-3 6-0
hypothesis_score = 5-7(4) 6-7(5) 6-3 6-0

# the hypothesis mentions the score of the match, which is also referenced in the premise
# however, the hypothesis refers to the score of a different match, which cannot be entailed from the premise
label = "neutral"

print(label)
