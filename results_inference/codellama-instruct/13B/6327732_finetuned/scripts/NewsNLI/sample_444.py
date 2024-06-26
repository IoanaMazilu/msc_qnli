wales_premise = 3
wales_hypothesis = 3
france_premise = 2
france_hypothesis = 2
scotland_premise = 1
scotland_hypothesis = 1

# the hypothesis mentions the ranking of Wales and France, which is also referenced in the premise
# however, the hypothesis does not mention the ranking of Scotland, which cannot be entailed from the premise
label = "neutral"

print(label)
