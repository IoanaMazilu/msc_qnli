soldiers_premise = 1917
soldiers_hypothesis = 1900

# the hypothesis mentions the number of soldiers dispatched by Rwanda, which is also mentioned in the premise
# however, the hypothesis approximates the number to 1900, which is less than the exact number reported in the premise
if soldiers_hypothesis < soldiers_premise:
    # check if the number of soldiers in the hypothesis contradicts the exact number reported in the premise
    label = "contradiction"
else:
    # if the number of soldiers in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "neutral"

print(label)
