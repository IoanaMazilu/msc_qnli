label = "neutral"

# The premise and hypothesis mention the same thing, so there is no contradiction
if premise == hypothesis:
    label = "entailment"

print(label)
