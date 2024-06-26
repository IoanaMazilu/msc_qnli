fruit_dinner_premise = 360
fruit_dinner_hypothesis = 360

# the hypothesis talks about the weight of the fruit Sue ate for dinner
# the same weight is also mentioned in the premise
if fruit_dinner_hypothesis >= fruit_dinner_premise:
    # check if the hypothesis value contradicts the premise's assertion of Sue eating 360 grams of fruit for dinner
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
