women_more_than_men_premise = 4
women_more_than_men_hypothesis = 1

# the hypothesis talks about the difference between the number of women and men, referenced also in the premise
if women_more_than_men_premise <= women_more_than_men_hypothesis:
    # check if the hypothesis value contradicts the established difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
