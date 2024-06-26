labels = ["entailment", "contradiction", "neutral"]

premise = "And one, the Stuxnet virus, was able to penetrate Iran's Natanz nuclear facility, researchers say."
hypothesis = "One such attack by Stuxnet virus able to penetrate Iran's Natanz nuclear facility."

penetration_premise = "penetrate"
penetration_hypothesis = "penetrate"

if penetration_hypothesis == penetration_premise:
    label = "entailment"
elif penetration_hypothesis < penetration_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
