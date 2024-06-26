subjects_premise = [40, 60, 70, 80, 80]
subjects_hypothesis = [40, 60, 70, 80, 80]

# the hypothesis refers to the scores obtained by Reeya in different subjects
if subjects_hypothesis[0] >= subjects_premise[0]:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif subjects_hypothesis[1]!= subjects_premise[1]:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif subjects_hypothesis[2]!= subjects_premise[2]:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif subjects_hypothesis[3]!= subjects_premise[3]:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif subjects_hypothesis[4]!= subjects_premise[4]:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif subjects_hypothesis[5]!= subjects_premise[5]:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and premise values do not contradict, we can infer entailment
    label = "entailment"

print(label)
