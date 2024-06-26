death_premise = "Hannover 96 and Germany goalkeeper Robert Enke from an apparent suicide has stunned the football world."
death_hypothesis = "Hannover and Germany international goalkeeper Robert Enke, 32, dies in apparent suicide."

# the premise and hypothesis mention the same event, which is a death in the football world
if death_hypothesis == death_premise:
    # if the hypothesis and premise mention the same event, we can infer entailment
    label = "entailment"
elif death_hypothesis > death_premise:
    # if the hypothesis mentions a higher number of deaths than the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise mention different events, we cannot infer any relation
    label = "neutral"

print(label)
