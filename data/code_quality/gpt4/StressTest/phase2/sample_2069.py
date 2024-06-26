height_increase_premise = 2
height_increase_hypothesis = 2

# the hypothesis refers to the impact of including Robert's height on the average, which is also mentioned in the premise
if height_increase_hypothesis < height_increase_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif height_increase_hypothesis > height_increase_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
