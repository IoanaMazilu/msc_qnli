wine_cellars_premise = 200
wine_cellars_hypothesis = 200

# the hypothesis mentions the number of wine cellars in Szepasszonyvolgy, which is also referenced in the premise
# however, the hypothesis does not mention anything about their accessibility from the center of Eger, which is stated in the premise
if wine_cellars_hypothesis != wine_cellars_premise:
    # check if the number of wine cellars in the hypothesis contradicts the number of wine cellars reported in the premise
    label = "contradiction"
else:
    # if the number of wine cellars in the hypothesis does not contradict the number of wine cellars in the premise, we can infer neutrality
    label = "neutral"

print(label)
