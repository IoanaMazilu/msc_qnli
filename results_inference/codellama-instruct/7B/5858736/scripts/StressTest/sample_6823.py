lilly_fish_premise = 80
lilly_fish_hypothesis = 10
rosy_fish_premise = 8
rosy_fish_hypothesis = 8

if lilly_fish_hypothesis <= lilly_fish_premise:
    label = "contradiction"
elif rosy_fish_hypothesis!= rosy_fish_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
