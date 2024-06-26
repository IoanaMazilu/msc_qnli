pink_highlighters_premise = 9
yellow_highlighters_premise = 8
blue_highlighters_premise = 5
pink_highlighters_hypothesis = 3
yellow_highlighters_hypothesis = 8
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of pink, yellow and blue highlighters in the teacher's desk
if pink_highlighters_hypothesis!= pink_highlighters_premise or yellow_highlighters_hypothesis!= yellow_highlighters_premise or blue_highlighters_hypothesis!= blue_highlighters_premise:
    label = "contradiction"
elif pink_highlighters_hypothesis == pink_highlighters_premise and yellow_highlighters_hypothesis == yellow_highlighters_premise and blue_highlighters_hypothesis == blue_highlighters_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
