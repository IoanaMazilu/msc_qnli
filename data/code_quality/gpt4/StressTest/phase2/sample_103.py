pink_highlighters_premise = 3
yellow_highlighters_premise = 2
blue_highlighters_premise = 5

pink_highlighters_hypothesis = 4
yellow_highlighters_hypothesis = 2
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of pink, yellow and blue highlighters in Kaya's teacher's desk, as mentioned in the premise
if pink_highlighters_hypothesis <= pink_highlighters_premise:
    # check if the number of pink highlighters in the hypothesis contradicts the estimate of more than 'pink_highlighters_premise' in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise or blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of yellow or blue highlighters in the hypothesis contradicts the number of yellow or blue highlighters reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pink highlighters and exact numbers for yellow and blue highlighters
    # the hypothesis is consistent with these, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
