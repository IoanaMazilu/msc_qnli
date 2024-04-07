# Premise: Jessica can text more than 75 words per minute, while Maurice can text 10 words per minute.
# Hypothesis: Jessica can text 95 words per minute, while Maurice can text 10 words per minute.
# Golden Label: neutral

jessica_texting_speed_premise = 75
maurice_texting_speed_premise = 10
jessica_texting_speed_hypothesis = 95
maurice_texting_speed_hypothesis = 10

# the hypothesis refers to both Jessica's and Maurice's texting speeds mentioned in the premise
if jessica_texting_speed_hypothesis <= jessica_texting_speed_premise:
    # check if the hypothesis value contradicts the estimate of more than 'jessica_texting_speed_premise'
    label = "contradiction"
elif maurice_texting_speed_hypothesis != maurice_texting_speed_premise:
    # check if the number of Maurice's texting speed in the hypothesis contradicts the number of Maurice's texting speed reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Jessica's texting speed
    # any number of words per minute greater than 'jessica_texting_speed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

