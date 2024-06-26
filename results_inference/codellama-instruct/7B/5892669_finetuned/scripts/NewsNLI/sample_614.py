killed_french_soldiers_premise = 4
killed_afghan_civilians_premise = 3
killed_french_soldiers_hypothesis = 5
killed_afghan_civilians_hypothesis = 1

# the hypothesis mentions the number of French soldiers and Afghan civilians killed, which are also mentioned in the premise
# however, the hypothesis refers to the number of killed French soldiers and the number of killed Afghan civilians, which cannot be entailed from the premise
label = "neutral"

print(label)
