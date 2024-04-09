soldiers_premise = 4
civilians_premise = 3

soldiers_hypothesis = 5
civilians_hypothesis = 1

# the hypothesis mentions the number of soldiers and civilians killed, which are also mentioned in the premise
# however, the hypothesis mentions a different number of soldiers killed than the premise
if soldiers_hypothesis!= soldiers_premise:
    # check if the number of soldiers killed in the hypothesis contradicts the number of soldiers killed in the premise
    label = "contradiction"
elif civilians_hypothesis!= civilians_premise:
    # check if the number of civilians killed in the hypothesis contradicts the number of civilians killed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
