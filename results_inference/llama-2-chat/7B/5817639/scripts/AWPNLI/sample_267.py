files_premise = float(4.0) + float(21.0) - float(23.0)
if files_hypothesis == 0.0:
    label = "entailment"
elif files_hypothesis < files_premise:
    label = "contradiction"
else:
    label = "contradiction"
print(label)
