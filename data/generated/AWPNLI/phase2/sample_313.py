# Premise: There are 43.0 pencils in the drawer and 19.0 pencils on the desk and Dan placed 16.0 more pencils on the desk.
# Hypothesis: 81.0 pencils are now there in total.
# Golden Label: contradiction

pencils_drawer_premise = 43.0
pencils_desk_premise = 19.0
added_pencils_premise = 16.0
total_pencils_hypothesis = 81.0

# the hypothesis refers to the total number of pencils, which are also mentioned in the premise
# compute the total number of pencils in the premise
total_pencils_premise = pencils_drawer_premise + pencils_desk_premise + added_pencils_premise
if total_pencils_hypothesis != total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

