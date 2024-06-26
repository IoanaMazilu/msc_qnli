women_ceos_premise = 18
women_ceos_hypothesis = 18

# the hypothesis mentions the number of women CEOs in the top 500 corporations, which is also mentioned in the premise
if women_ceos_hypothesis!= women_ceos_premise:
    # check if the number of women CEOs from the hypothesis contradicts the number of women CEOs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
