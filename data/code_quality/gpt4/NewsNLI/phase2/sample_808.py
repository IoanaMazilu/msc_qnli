killed_premise = 3
wounded_premise = 4
killed_hypothesis = 11
wounded_hypothesis = 12

# the hypothesis mentions the number of killed and wounded civilians, which are also mentioned in the premise
# however, the hypothesis refers to multiple bombings and gives different numbers for killed and wounded
# we need to check if the numbers from the hypothesis contradict the numbers from the premise
if killed_hypothesis < killed_premise or wounded_hypothesis < wounded_premise:
    label = "contradiction"
else:
    # if the number of killed and wounded in the hypothesis do not contradict the premise, we infer neutrality
    label = "neutral"

print(label)
