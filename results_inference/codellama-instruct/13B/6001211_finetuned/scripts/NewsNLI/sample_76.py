favor_premise = 52
favor_hypothesis = 52
oppose_premise = 46

# the hypothesis mentions the percentage of people favoring the war, which is also referenced in the premise
# however, the hypothesis does not mention the percentage of people opposing the war, which is present in the premise
if favor_hypothesis!= favor_premise:
    # check if the percentage of people favoring the war in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the percentage of people favoring the war in the hypothesis does not contradict the percentage in the premise, we can infer neutrality
    label = "neutral"

print(label)
