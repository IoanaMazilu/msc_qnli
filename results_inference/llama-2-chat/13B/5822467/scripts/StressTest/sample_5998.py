# define variables for the numerical entities in the premise and hypothesis
top_10_lists_premise = 4/4  # at least less than 4/4 of the top-10-movies lists
top_10_lists_hypothesis = 1/4  # at least 1/4 of the top-10-movies lists
members_premise = 760  # members of the Cinematic Academy

# extract the numerical entities from the premise and hypothesis
top_10_lists_premise_value = int(top_10_lists_premise * 100)  # 400
top_10_lists_hypothesis_value = int(top_10_lists_hypothesis * 100)  # 100
members_premise_value = int(members_premise)  # 760

# compare the numerical entities
if top_10_lists_premise_value > top_10_lists_hypothesis_value:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"
elif top_10_lists_premise_value <= top_10_lists_hypothesis_value:
    # the hypothesis refers to a lower percentage of top-10-movies lists than the premise
    label = "contradiction"
else:
    # the hypothesis refers to a higher percentage of top-10-movies lists than the premise
    label = "entailment"

print(label)
