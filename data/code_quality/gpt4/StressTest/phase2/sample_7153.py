pink_highlighters_premise = 7
pink_highlighters_hypothesis = 9
yellow_highlighters_premise = 8
yellow_highlighters_hypothesis = 8
blue_highlighters_premise = 5
blue_highlighters_hypothesis = 5

# the hypothesis talks about the number of highlighters in a teacher's desk, referenced also in the premise
if pink_highlighters_hypothesis <= pink_highlighters_premise:
    # check if the hypothesis value contradicts the estimate of more than 'pink_highlighters_premise'
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise or blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of yellow or blue highlighters in the hypothesis contradicts the number of such highlighters reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pink highlighters
    # any number of pink highlighters greater than 'pink_highlighters_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
