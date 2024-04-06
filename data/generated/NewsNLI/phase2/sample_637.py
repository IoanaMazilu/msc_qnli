# Premise: On it she had quickly scrawled two words:'' It's over.''
# Hypothesis: Lawyer's two words told him his fate:'' It's over''
# Golden Label: neutral

words_premise = 2
words_hypothesis = 2

# the hypothesis mentions the number of words, which is also mentioned in the premise

if words_hypothesis != words_premise:
    # check if the number of words in the hypothesis contradicts the number of words in the premise
    label = "contradiction"
else:
    # if the number of words in the hypothesis does not contradict the number of words in the premise, we can infer entailment
    label = "entailment"

print(label)

