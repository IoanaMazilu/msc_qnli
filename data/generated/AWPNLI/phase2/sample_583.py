# Premise: Josh had 142.0 pencils and he got 31.0 pencils from Dorothy.
# Hypothesis: Josh has 168.0 pencils now.
# Golden Label: contradiction

pencils_initial_premise = 142.0
received_pencils_premise = 31.0
total_pencils_hypothesis = 168.0

# the hypothesis refers to the total number of pencils, which is also mentioned in the premise
# compute the total number of pencils in the premise
total_pencils_premise = pencils_initial_premise + received_pencils_premise
if total_pencils_hypothesis != total_pencils_premise:
    # check if the total number of pencils in the hypothesis contradicts the total number of pencils from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

