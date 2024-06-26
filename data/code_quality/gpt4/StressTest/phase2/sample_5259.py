rainfall_premise = 35
rainfall_hypothesis = 55

# the hypothesis refers to the total rainfall in Springdale during the first two weeks of May
if rainfall_hypothesis <= rainfall_premise:
    # check if the upper limit suggested by the hypothesis contradicts the exact value from the premise
    label = "contradiction"
elif rainfall_premise > rainfall_hypothesis:
    # check if the value of rainfall in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
