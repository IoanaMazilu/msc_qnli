aaron_jelly_beans_premise = 7
aaron_jelly_beans_hypothesis = 5
bianca_jelly_beans_premise = 7
bianca_jelly_beans_hypothesis = 7
callie_jelly_beans_premise = 8
callie_jelly_beans_hypothesis = 8
dante_jelly_beans_premise = 13
dante_jelly_beans_hypothesis = 13

# the hypothesis talks about the number of jelly beans each child has
# we need to check if the number of jelly beans each child has in the hypothesis contradicts the number of jelly beans each child has in the premise
if aaron_jelly_beans_hypothesis < aaron_jelly_beans_premise:
    label = "contradiction"
elif bianca_jelly_beans_hypothesis!= bianca_jelly_beans_premise:
    label = "contradiction"
elif callie_jelly_beans_hypothesis!= callie_jelly_beans_premise:
    label = "contradiction"
elif dante_jelly_beans_hypothesis!= dante_jelly_beans_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
