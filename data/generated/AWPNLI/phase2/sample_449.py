# Premise: A petri dish originally contained 600.0 bacteria and a scientist let the bacteria grow, and now there are 8917.0 more of them.
# Hypothesis: 9513.0 bacteria are there now.
# Golden Label: contradiction

original_bacteria_premise = 600.0
additional_bacteria_premise = 8917.0
total_bacteria_hypothesis = 9513.0

# the hypothesis refers to the total number of bacteria, which is also mentioned in the premise
# compute the total number of bacteria in the premise
total_bacteria_premise = original_bacteria_premise + additional_bacteria_premise
if total_bacteria_hypothesis != total_bacteria_premise:
    # check if the total number of bacteria in the hypothesis contradicts the total number of bacteria from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

