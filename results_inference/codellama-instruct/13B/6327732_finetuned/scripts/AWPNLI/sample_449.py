initial_bacteria_premise = 600.0
grown_bacteria_premise = 8917.0
total_bacteria_hypothesis = 9513.0

# the hypothesis refers to the total number of bacteria, which are also mentioned in the premise
# compute the total number of bacteria in the premise
total_bacteria_premise = initial_bacteria_premise + grown_bacteria_premise
if total_bacteria_hypothesis!= total_bacteria_premise:
    # check if the number of bacteria in the hypothesis contradicts the number of bacteria from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
