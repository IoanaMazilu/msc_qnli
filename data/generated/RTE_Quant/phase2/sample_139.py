# Premise: Romania currently supplies one of the world's largest contingents of troops in Iraq, with nearly 1000 people.
# Hypothesis: Romania sent 730 troops in Iraq.
# Golden Label: neutral

troops_premise = 1000
troops_hypothesis = 730

# the hypothesis talks about the number of troops Romania sent in Iraq, which is mentioned in the premise as well
if troops_hypothesis > troops_premise:
    # check if the number of troops in the hypothesis exceeds the number of troops from the premise
    label = "contradiction"
elif troops_hypothesis <= troops_premise:
    # if the number of troops in the hypothesis does not exceed the number of troops in the premise, we can infer entailment
    label = "entailment"

print(label)

