women_premise = 2
women_hypothesis = 2

# the hypothesis mentions the number of women trapped inside a house, which is also mentioned in the premise
# however, the hypothesis does not mention anything about the dogs, which is mentioned in the premise
if women_hypothesis!= women_premise:
    # check if the number of women in the hypothesis contradicts the number of women mentioned in the premise
    label = "contradiction"
else:
    # if the number of women in the hypothesis does not contradict the number of women in the premise, we can infer neutrality
    label = "neutral"

print(label)