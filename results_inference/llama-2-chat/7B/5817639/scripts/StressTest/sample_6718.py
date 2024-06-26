jelly_beans_premise = {
    "Aaron": 5,
    "Bianca": 7,
    "Callie": 8,
    "Dante": 13
}

jelly_beans_hypothesis = {
    "Aaron": 5,
    "Bianca": 7,
    "Callie": 8,
    "Dante": 13
}

# the hypothesis talks about the number of jelly beans each child has, consistent with the premise
if jelly_beans_hypothesis["Aaron"] <= jelly_beans_premise["Aaron"]:
    # check if the hypothesis value contradicts the estimate of less than 'jelly_beans_premise["Aaron"]'
    label = "contradiction"
elif jelly_beans_hypothesis["Bianca"]!= jelly_beans_premise["Bianca"] or jelly_beans_hypothesis["Callie"]!= jelly_beans_premise["Callie"] or jelly_beans_hypothesis["Dante"]!= jelly_beans_premise["Dante"]:
    # check if any aspect of the hypothesis contradicts any aspect of the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
