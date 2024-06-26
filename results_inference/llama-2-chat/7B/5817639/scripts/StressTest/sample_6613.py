students_premise = {
    "Random-processing methods": 112,
    "Scramjet rocket engines": 234,
    "both": 112
}

hypothesis = {
    "Random-processing methods": 312,
    "Scramjet rocket engines": 234,
    "both": 112
}

# compare the hypothesis with the premise values
if hp.get("Random-processing methods") <= premise.get("Random-processing methods"):
    label = "contradiction"
elif hp.get("Scramjet rocket engines")!= premise.get("Scramjet rocket engines"):
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
