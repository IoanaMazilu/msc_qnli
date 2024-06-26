investigation_premise = 3
investigation_hypothesis = 3

# Both the premise and hypothesis mention investigation of possible murder of three young boys
# Both also mention investigation of sexual abuse

if investigation_hypothesis != investigation_premise:
    # check if the number of investigations in the hypothesis contradicts the number of investigations in the premise
    label = "contradiction"
else:
    # if the number of investigations in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)
