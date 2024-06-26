jessica_texting_speed_premise = 95
jessica_texting_speed_hypothesis = 15
maurice_texting_speed_premise = 10
maurice_texting_speed_hypothesis = 10

# the hypothesis refers to the texting speed of Jessica and Maurice mentioned in the premise
if jessica_texting_speed_hypothesis != jessica_texting_speed_premise:
    # check if the texting speed of Jessica in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif maurice_texting_speed_hypothesis != maurice_texting_speed_premise:
    # check if the texting speed of Maurice in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
