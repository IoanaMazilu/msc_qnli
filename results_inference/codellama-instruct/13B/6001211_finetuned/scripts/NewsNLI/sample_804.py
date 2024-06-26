bombs_karbala_premise = 2
bombs_karbala_hypothesis = 2
bombs_baghdad_hypothesis = 1

# the hypothesis mentions the number of bombs that hit in Karbala, which is also referenced in the premise
# however, the hypothesis also mentions a bomb hitting in Baghdad, which cannot be entailed from the premise
if bombs_karbala_hypothesis!= bombs_karbala_premise:
    # check if the number of bombs in Karbala in the hypothesis contradicts the number of bombs reported in the premise
    label = "contradiction"
else:
    # if the number of bombs in Karbala in the hypothesis does not contradict the number of bombs in the premise, we can infer neutrality
    label = "neutral"

print(label)
