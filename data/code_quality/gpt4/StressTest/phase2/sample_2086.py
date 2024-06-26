jessica_text_rate_premise = 25
maurice_text_rate_premise = 55
jessica_text_rate_hypothesis = 85
maurice_text_rate_hypothesis = 55

# the hypothesis refers to the text rates of Jessica and Maurice as mentioned in the premise
if jessica_text_rate_hypothesis <= jessica_text_rate_premise:
    # check if the text rate of Jessica in the hypothesis contradicts the premise
    label = "contradiction"
elif maurice_text_rate_hypothesis != maurice_text_rate_premise:
    # check if the text rate of Maurice in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jessica's text rate
    # any text rate of Jessica greater than jessica_text_rate_premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
