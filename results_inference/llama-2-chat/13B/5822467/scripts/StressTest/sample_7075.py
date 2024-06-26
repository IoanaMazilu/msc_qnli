rank_premise = 15
rank_hypothesis = 65
class_size_premise = 182

# the hypothesis refers to Veena's rank and the class size mentioned in the premise
if rank_hypothesis <= rank_premise:
    # check if the estimate of 'rank_hypothesis' contradicts the rank reported in the premise
    label = "contradiction"
elif rank_hypothesis > rank_premise:
    # check if the rank in the hypothesis is greater than the rank reported in the premise
    label = "entailment"
else:
    # the premise gives only an estimate for Veena's rank
    # any rank between 15 and 65 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
