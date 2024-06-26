premise_jelly_beans = 1
hypothesis_jelly_beans = 7

if premise_jelly_beans <= hypothesis_jelly_beans:
    label = "entailment"
else:
    label = "contradiction"

print(label)
