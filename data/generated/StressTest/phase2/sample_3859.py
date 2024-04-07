# Premise: The instructions state that Cheryl needs less than 8 square yards of one type of material and 1/2 square yards of another type of material for a project.
# Hypothesis: The instructions state that Cheryl needs 2 square yards of one type of material and 1/2 square yards of another type of material for a project.
# Golden Label: neutral

material1_premise = 8
material1_hypothesis = 2
material2_premise = 1/2
material2_hypothesis = 1/2

# the hypothesis refers to the amount of two types of materials mentioned in the premise
if material1_hypothesis >= material1_premise:
    # check if the amount of 'material1_hypothesis' contradicts the premise of less than 'material1_premise'
    label = "contradiction"
elif material2_hypothesis != material2_premise:
    # check if the amount of 'material2_hypothesis' contradicts the amount of 'material2_premise' in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

