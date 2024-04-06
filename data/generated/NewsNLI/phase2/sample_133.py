# Premise: Szepasszonyvolgy and its more than 200 wine cellars are easily reached from the center of Eger via the miniature train that departs from Egeszseghaz Street.
# Hypothesis: Szepasszonyvolgy, or the Valley of the Beautiful Women, contains more than 200 wine cellars.
# Golden Label: entailment

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

