# Define variables for premise and hypothesis
authorities_premise = 4
suspects_hypothesis = 4
gun_attack_premise = 1
hostages_hypothesis = 0

# Check if the number of suspects in the hypothesis contradicts the number of suspects in the premise
if suspects_hypothesis!= authorities_premise:
    label = "contradiction"

# Check if the presence of a gun attack in the hypothesis contradicts the absence of a gun attack in the premise
if gun_attack_hypothesis!= gun_attack_premise:
    label = "contradiction"

# If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
elif suspects_hypothesis == authorities_premise and gun_attack_hypothesis == gun_attack_premise:
    label = "entailment"

print(label)
