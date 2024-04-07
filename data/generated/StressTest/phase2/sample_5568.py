# Premise: Jessica can text 75 words per minute, while Maurice can text 10 words per minute.
# Hypothesis: Jessica can text more than 35 words per minute, while Maurice can text 10 words per minute.
# Golden Label: entailment

jessica_texting_rate_premise = 75
maurice_texting_rate_premise = 10
jessica_texting_rate_hypothesis = 35
maurice_texting_rate_hypothesis = 10

# the hypothesis talks about the texting rate of Jessica and Maurice, referenced also in the premise
if jessica_texting_rate_hypothesis >= jessica_texting_rate_premise:
    # check if the hypothesis value contradicts the value of 'jessica_texting_rate_premise'
    label = "contradiction"
elif maurice_texting_rate_hypothesis != maurice_texting_rate_premise:
    # check if the number of words Maurice can text in the hypothesis contradicts the number of words Maurice can text in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

