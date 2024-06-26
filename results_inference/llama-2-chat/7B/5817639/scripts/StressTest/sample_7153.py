pink_highlighters_premise = 7
yellow_highlighters_premise = 8
blue_highlighters_premise = 5

hypothesis_pink_highlighters = 9
hypothesis_yellow_highlighters = 8
hypothesis_blue_highlighters = 5

# the hypothesis talks about the number of highlighters in Kaya's teacher's desk, referenced also in the premise
if hypothesis_pink_highlighters <= pink_highlighters_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pink_highlighters_premise'
    label = "contradiction"
elif hypothesis_yellow_highlighters!= yellow_highlighters_premise:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
