sand_premise = 0.16666666666666666
dirt_premise = 0.3333333333333333
cement_premise = 0.16666666666666666
total_materials_hypothesis = 0.6666666667

# the hypothesis refers to the total amount of materials (sand, dirt, cement), which are also mentioned in the premise
# compute the total amount of materials in the premise
total_materials_premise = sand_premise + dirt_premise + cement_premise

if total_materials_hypothesis != total_materials_premise:
    # check if the total amount of materials in the hypothesis contradicts the total amount of materials from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
