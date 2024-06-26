concerned_premise = 0.33
not_concerned_premise = 0.69
worried_hypothesis = 0.52

# the hypothesis mentions the percentage of Americans worried about a bridge collapse, which is also referenced in the premise
# however, the hypothesis does not mention the percentage of Americans who are not worried, which is indicated in the premise
# thus, we cannot fully entail the hypothesis from the premise
label = "neutral"

print(label)
