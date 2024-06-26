age_premise = 71
age_hypothesis = 71
num_kids_premise = 3
num_kids_hypothesis = 3
num_grandkids_premise = 13
num_grandkids_hypothesis = 13
num_great_grandkids_premise = 1
num_great_grandkids_hypothesis = 1

# the hypothesis mentions the same number of kids, grandkids, and great-grandkids as the premise
# however, the order of the entities is different in the hypothesis
# therefore, we cannot infer entailment or contradiction
label = "neutral"

print(label)
