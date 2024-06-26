# The hypothesis refers to the same situation as the premise, so we can use the same variables
england_premise = 6
england_hypothesis = 3
france_premise = 6
france_hypothesis = 11
italy_premise = 0
italy_hypothesis = 0

# The hypothesis does not contradict the premise
if england_hypothesis!= england_premise:
    label = "contradiction"
elif france_hypothesis!= france_premise:
    label = "contradiction"
elif italy_hypothesis!= italy_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
