women_victims_premise = 2
men_victims_premise = 2
total_victims_premise = women_victims_premise + men_victims_premise

women_victims_hypothesis = 2
men_victims_hypothesis = 2
total_victims_hypothesis = women_victims_hypothesis + men_victims_hypothesis

# the hypothesis mentions the total number of victims (men and women), which is also mentioned in the premise
# however, the hypothesis does not mention the age range of the victims, which is information included in the premise
if total_victims_hypothesis != total_victims_premise:
    # check if the total number of victims in the hypothesis contradicts the total number of victims reported in the premise
    label = "contradiction"
else:
    # if the total number of victims in the hypothesis does not contradict the premise, we infer neutrality because the age of the victims is not discussed in the hypothesis
    label = "neutral"

print(label)
