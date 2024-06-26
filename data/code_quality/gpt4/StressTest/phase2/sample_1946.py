bread_dinner_premise = 240
bread_dinner_hypothesis = 240

# the hypothesis refers to the amount of bread eaten by Cara for dinner, which is also mentioned in the premise
if bread_dinner_hypothesis <= bread_dinner_premise:
    # check if the hypothesis value contradicts the premise value for the amount of bread eaten for dinner
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
