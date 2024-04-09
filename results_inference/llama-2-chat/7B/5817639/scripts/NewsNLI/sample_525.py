expert_opinion_premise = "expert says"
open_source_anti_bribe_sites_hypothesis = "open-source anti-bribe sites"

# compare the number of words in the premise and hypothesis to determine if they are similar
if len(expert_opinion_premise) == len(open_source_anti_bribe_sites_hypothesis):
    # if the number of words is the same, proceed to compare the words themselves
    words = expert_opinion_premise.split()
    hypothesis_words = open_source_anti_bribe_sites_hypothesis.split()
    for word in words:
        if word not in hypothesis_words:
            # if a word in the premise is not in the hypothesis, it contradicts the premise
            label = "contradiction"
            break
    else:
        # if all words in the premise are also in the hypothesis, we can infer entailment
        label = "entailment"
else:
    # if the number of words is different, the hypotheses do not contradict each other
    label = "neutral"

print(label)
