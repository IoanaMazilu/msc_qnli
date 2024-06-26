women_premise = 4
men_premise = 4
women_hypothesis = 6
men_hypothesis = 6

# the hypothesis refers to the number of women and men on the board of education, mentioned in the premise
if women_premise <= women_hypothesis:
    # check if the estimate of 'women_hypothesis' contradicts the number of women in the premise
    label = "contradiction"
elif men_hypothesis!= men_premise:
    # check if the number of men in the hypothesis contradicts the number of men reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
