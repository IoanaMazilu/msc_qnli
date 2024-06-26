supply_premise = 14797.0
supply_hypothesis = 9832.0

# the hypothesis talks about the number of bathing suits for men, which is also mentioned in the premise
# compute the total number of bathing suits for men in the premise
total_men_premise = supply_premise - supply_hypothesis

# check if the number of bathing suits for men in the hypothesis contradicts the number of bathing suits for men in the premise
if total_men_hypothesis < total_men_premise:
    label = "contradiction"
elif supply_hypothesis < supply_premise:
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
