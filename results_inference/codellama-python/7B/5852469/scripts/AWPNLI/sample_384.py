verbs_morning_premise = 35
verbs_evening_premise = 10
verbs_hypothesis = 50 
nouns_premise = 5
nouns_hypothesis = 5

# the hypothesis talks about the number of learned nouns and verbs, which are also referenced in the premise
# find the total number of verbs learned from the premise 
total_verbs_premise = verbs_morning_premise + verbs_evening_premise
if max_verbs_hypothesis >= total_verbs_premise:
    # check if the total verbs from the hypothesis contradict the estimate of more than'verbs_evening_premise'
    label = "contradiction"
elif nouns_hypothesis!= nouns_premise:
    # check if the number of nouns from the hypothesis contradicts the number of nouns in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"
    
print(label)
