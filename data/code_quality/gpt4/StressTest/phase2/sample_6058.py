anita_premise = 38
indu_premise = 27
geeta_premise = 36

anita_hypothesis = 18
indu_hypothesis = 27
geeta_hypothesis = 36

# the hypothesis refers to the work efficiency of Anita, Indu and Geeta mentioned in the premise
if anita_hypothesis >= anita_premise:
    # check if the time 'anita_hypothesis' contradicts the time required by Anita in the premise
    label = "contradiction"
elif indu_hypothesis < indu_premise:
    # check if the time 'indu_hypothesis' contradicts the time required by Indu in the premise
    label = "contradiction"
elif geeta_hypothesis < geeta_premise:
    # check if the time 'geeta_hypothesis' contradicts the time required by Geeta in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
