# Premise: Jessica can text 125 words per minute, while Maurice can text 10 words per minute.
# Hypothesis: Jessica can text 325 words per minute, while Maurice can text 10 words per minute.
# Golden Label: contradiction

jessica_text_speed_premise = 125
maurice_text_speed_premise = 10
jessica_text_speed_hypothesis = 325
maurice_text_speed_hypothesis = 10

# the hypothesis refers to the text speed of both Jessica and Maurice mentioned in the premise
if jessica_text_speed_hypothesis != jessica_text_speed_premise:
    # check if the text speed of Jessica in the hypothesis contradicts the text speed of Jessica reported in the premise
    label = "contradiction"
elif maurice_text_speed_hypothesis != maurice_text_speed_premise:
    # check if the text speed of Maurice in the hypothesis contradicts the text speed of Maurice reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

