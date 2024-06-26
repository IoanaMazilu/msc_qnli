bombs_premise = 2
bombs_hypothesis = 2

# the hypothesis mentions the number of bombs in Karbala and Baghdad, which is also mentioned in the premise
# however, the premise only mentions two bombs in Karbala, while the hypothesis mentions one bomb in Baghdad

if bombs_hypothesis!= bombs_premise:
    # check if the number of bombs in the hypothesis contradicts the number of bombs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
