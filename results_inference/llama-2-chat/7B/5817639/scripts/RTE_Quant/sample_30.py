# Variables for premise and hypothesis
nato_members_premise = 19
nato_members_hypothesis = 16

# Check if the number of NATO members in the hypothesis contradicts the premise
if nato_members_hypothesis!= nato_members_premise:
    label = "contradiction"
elif nato_members_hypothesis < nato_members_premise:
    # Check if the number of NATO members in the hypothesis is less than the number in the premise
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
