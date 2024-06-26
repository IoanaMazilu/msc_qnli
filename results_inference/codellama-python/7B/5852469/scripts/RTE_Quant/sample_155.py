judges_premise = 8
judges_hypothesis = 11

# the hypothesis does not contradict the premise, since the number of judges in the Yugoslavia war tribunal is not mentioned in the premise
if judges_hypothesis!= judges_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
