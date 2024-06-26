men_women_ratio_premise = 4 / 5
men_women_ratio_hypothesis = 3 / 5

# the hypothesis refers to the ratio of men to women in the same choir mentioned in the premise
if men_women_ratio_premise <= men_women_ratio_hypothesis:
    # check if the hypothesis value contradicts the ratio of men to women in the premise
    label = "contradiction"
elif men_women_ratio_premise > men_women_ratio_hypothesis:
    # if the ratio of men to women in the premise is more than the ratio in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
