# Premise: Ayesha's father was more than 24 years of age when she was born while her mother was 30 years old when her brother four years younger to her was born.
# Hypothesis: Ayesha's father was 34 years of age when she was born while her mother was 30 years old when her brother four years younger to her was born.
# Golden Label: neutral

father_age_premise = 24
father_age_hypothesis = 34
mother_age_premise = 30
mother_age_hypothesis = 30

# the hypothesis talks about the ages of Ayesha's parents at the time of her and her brother's birth, also mentioned in the premise
if father_age_hypothesis <= father_age_premise:
    # check if the hypothesis contradicts the premise which states the father's age was more than 'father_age_premise'
    label = "contradiction"
elif mother_age_hypothesis != mother_age_premise:
    # check if the mother's age at the time of the brother's birth in the hypothesis contradicts the same age reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the father's age
    # any age greater than 'father_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

