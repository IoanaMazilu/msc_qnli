# Premise: Jessica can text more than 35 words per minute, while Maurice can text 10 words per minute.
# Hypothesis: Jessica can text 75 words per minute, while Maurice can text 10 words per minute.
# Golden Label: neutral

jessica_text_speed_premise = 35
jessica_text_speed_hypothesis = 75
maurice_text_speed_premise = 10
maurice_text_speed_hypothesis = 10

# the hypothesis refers to the text speed of Jessica and Maurice mentioned in the premise
if jessica_text_speed_hypothesis <= jessica_text_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jessica_text_speed_premise'
    label = "contradiction"
elif maurice_text_speed_hypothesis != maurice_text_speed_premise:
    # check if the text speed of Maurice in the hypothesis contradicts the text speed of Maurice reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the text speed of Jessica
    # any text speed of Jessica greater than 'jessica_text_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

