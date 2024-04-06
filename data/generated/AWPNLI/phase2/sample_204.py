# Premise: A sandbox is 312.0 centimeters long and 146.0 centimeters wide.
# Hypothesis: The sandbox covers 45552.0 square centimeters of ground.
# Golden Label: entailment

length_sandbox_premise = 312.0
width_sandbox_premise = 146.0
area_sandbox_hypothesis = 45552.0

# the hypothesis mentions the area covered by the sandbox which is the product of its length and width
# compute the area of the sandbox using the premise
area_sandbox_premise = length_sandbox_premise * width_sandbox_premise
if area_sandbox_hypothesis != area_sandbox_premise:
    # check if the area of the sandbox in the hypothesis contradicts the area calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

