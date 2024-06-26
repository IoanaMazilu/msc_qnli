billion_premise = 1000000000
billion_hypothesis = 1000000000
trillion_premise = 1000000000000
trillion_hypothesis = 1000000000000

# the hypothesis talks about the definitions of billion and trillion, which are also mentioned in the premise
if billion_hypothesis!= billion_premise:
    label = "contradiction"
elif trillion_hypothesis!= trillion_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
