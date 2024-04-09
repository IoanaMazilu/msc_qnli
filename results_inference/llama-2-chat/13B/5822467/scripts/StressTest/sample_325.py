amar_premise = 84
bhavan_premise = 36
chetan_premise = 44

amar_hypothesis = 64
bhavan_hypothesis = 36
chetan_hypothesis = 44

# the hypothesis refers to the scores of Amar, Bhavan, and Chetan in the exam
if amar_hypothesis > amar_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif bhavan_hypothesis!= bhavan_premise:
    # the number of points scored by Bhavan in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif chetan_hypothesis!= chetan_premise:
    # the number of points scored by Chetan in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if all the scores in the hypothesis are consistent with the premise, we can infer neutrality
    label = "neutral"

print(label)
