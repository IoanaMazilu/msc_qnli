# Premise: Jessica can text less than 225 words per minute, while Maurice can text 10 words per minute.
# Hypothesis: Jessica can text 125 words per minute, while Maurice can text 10 words per minute.
# Golden Label: neutral

jessica_texting_speed_premise = 225
jessica_texting_speed_hypothesis = 125
maurice_texting_speed_premise = 10
maurice_texting_speed_hypothesis = 10

# the hypothesis refers to the texting speed of both Jessica and Maurice mentioned in the premise
if jessica_texting_speed_hypothesis >= jessica_texting_speed_premise:
    # check if the 'jessica_texting_speed_hypothesis' contradicts the upper limit of Jessica's texting speed in the premise
    label = "contradiction"
elif maurice_texting_speed_hypothesis != maurice_texting_speed_premise:
    # check if the Maurice's texting speed in the hypothesis contradicts Maurice's texting speed in the premise
    label = "contradiction"
elif jessica_texting_speed_hypothesis < jessica_texting_speed_premise and maurice_texting_speed_hypothesis == maurice_texting_speed_premise:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

