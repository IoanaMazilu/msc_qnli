jessica_text_speed_premise = 75
maurice_text_speed_premise = 25
jessica_text_speed_hypothesis = 85
maurice_text_speed_hypothesis = 25

# the hypothesis talks about the text speed of Jessica and Maurice, referenced also in the premise
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
