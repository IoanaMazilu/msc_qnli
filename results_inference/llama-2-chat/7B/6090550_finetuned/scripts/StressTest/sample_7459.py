# The premise and hypothesis both refer to the same situation, but they have different conditions
# The premise mentions that the film must appear in less than 2/4 of the top-10 lists, while the hypothesis states it must appear in at least 1/4

# To determine if the hypothesis contradicts or entails the premise, we need to compare the conditions
# If the condition in the hypothesis is less than the condition in the premise, then it's a contradiction
if (2/4) <= 1/4:
    label = "contradiction"
else:
    label = "entailment"

print(label)
