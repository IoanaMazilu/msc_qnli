pink_highlighters_premise = 9
yellow_highlighters_premise = 8
blue_highlighters_premise = 5

pink_highlighters_hypothesis = 3
yellow_highlighters_hypothesis = 8
blue_highlighters_hypothesis = 5

# the hypothesis talks about the number of each color of highlighters in Kaya's teacher's desk, which is also mentioned in the premise
if pink_highlighters_hypothesis!= pink_highlighters_premise or yellow_highlighters_hypothesis!= yellow_highlighters_premise or blue_highlighters_hypothesis!= blue_highlighters_premise:
    # check if the number of each color of highlighters in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
