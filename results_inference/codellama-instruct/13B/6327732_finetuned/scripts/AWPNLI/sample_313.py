pencils_drawer_premise = 43.0
pencils_desk_premise = 19.0
pencils_desk_hypothesis = 81.0

# the hypothesis refers to the total number of pencils, which are also mentioned in the premise
# compute the total number of pencils in the premise
total_pencils_premise = pencils_drawer_premise + pencils_desk_premise
if pencils_desk_hypothesis!= total_pencils_premise:
    # check if the number of pencils in the hypothesis contradicts the number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)