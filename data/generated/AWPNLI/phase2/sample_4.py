# Premise: There are 2.0 pencils in the drawer and Tim placed 3.0 pencils in the drawer.
# Hypothesis: 5.0 pencils are now there in total.
# Golden Label: entailment

pencils_drawer_premise = 2.0
pencils_tim_placed = 3.0
total_pencils_hypothesis = 5.0

# the hypothesis refers to the total number of pencils, which is calculated in the premise
# calculate the total number of pencils in the premise
total_pencils_premise = pencils_drawer_premise + pencils_tim_placed
if total_pencils_hypothesis != total_pencils_premise:
    # check if the total number of pencils in the hypothesis contradicts the total number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

