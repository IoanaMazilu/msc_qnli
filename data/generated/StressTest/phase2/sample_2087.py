# Premise: Jessica can text 85 words per minute, while Maurice can text 55 words per minute.
# Hypothesis: Jessica can text 65 words per minute, while Maurice can text 55 words per minute.
# Golden Label: contradiction

jessica_texting_speed_premise = 85
maurice_texting_speed_premise = 55
jessica_texting_speed_hypothesis = 65
maurice_texting_speed_hypothesis = 55

# the hypothesis talks about the texting speeds of Jessica and Maurice, also mentioned in the premise
if jessica_texting_speed_hypothesis > jessica_texting_speed_premise:
    # check if the hypothesis value contradicts Jessica's texting speed in the premise
    label = "contradiction"
elif maurice_texting_speed_hypothesis != maurice_texting_speed_premise:
    # check if the hypothesis value contradicts Maurice's texting speed in the premise
    label = "contradiction"
elif jessica_texting_speed_hypothesis < jessica_texting_speed_premise:
    # Jessica's texting speed in the hypothesis is less than that in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

