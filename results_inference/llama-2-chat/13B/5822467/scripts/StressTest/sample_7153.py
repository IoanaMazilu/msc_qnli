pink_highlighters_premise = 7
pink_highlighters_hypothesis = 9
yellow_highlighters_premise = 8
yellow_highlighters_hypothesis = 8
blue_highlighters_premise = 5

# the hypothesis refers to the number of each type of highlighter in the teacher's desk
if pink_highlighters_hypothesis <= pink_highlighters_premise and \
   yellow_highlighters_hypothesis == yellow_highlighters_premise and \
   blue_highlighters_hypothesis == blue_highlighters_premise:
    # all hypothesis values match the premise values, so we can infer entailment
    label = "entailment"
elif pink_highlighters_hypothesis > pink_highlighters_premise or \
     yellow_highlighters_hypothesis!= yellow_highlighters_premise or \
     blue_highlighters_hypothesis!= blue_highlighters_premise:
    # at least one aspect in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
