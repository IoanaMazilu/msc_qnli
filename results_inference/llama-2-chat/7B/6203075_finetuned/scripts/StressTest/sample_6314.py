males_premise = 4
males_hypothesis = 4
females_premise = 3
females_hypothesis = 3
male_to_male_premise = 0
male_to_male_hypothesis = 0
female_to_female_premise = 0
female_to_female_hypothesis = 0
mary_sitting_premise = True
mary_sitting_hypothesis = True

# the hypothesis refers to the number of males and females sitting, which is also mentioned in the premise
if males_hypothesis!= males_premise:
    label = "contradiction"
elif females_hypothesis!= females_premise:
    label = "contradiction"
elif male_to_male_hypothesis!= male_to_male_premise:
    label = "contradiction"
elif female_to_female_hypothesis!= female_to_female_premise:
    label = "contradiction"
elif mary_sitting_hypothesis!= mary_sitting_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
