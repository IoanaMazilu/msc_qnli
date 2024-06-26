women_premise = 19
men_premise = 5

# define variables for the hypothesis
women_hypothesis = 19
men_hypothesis = 5

# check if the number of women in the hypothesis contradicts the number of women in the premise
if women_hypothesis!= women_premise:
    # if the number of women in the hypothesis contradicts the number of women in the premise, then we have a contradiction
    label = "contradiction"
elif men_hypothesis!= men_premise:
    # if the number of men in the hypothesis contradicts the number of men in the premise, then we have a contradiction
    label = "contradiction"
else:
    # if the number of women and men in the hypothesis and premise are the same, then we have neutrality
    label = "neutral"

print(label)
