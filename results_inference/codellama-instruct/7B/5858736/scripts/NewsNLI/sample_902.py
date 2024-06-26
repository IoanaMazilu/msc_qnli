premise_reid_re_elected = True
premise_other_top_members_re_elected = True
premise_centrist_members_voted_against_reid = True

hypothesis_warren_joined_senate_democratic_leadership_team = True

# the hypothesis mentions the addition of Warren to the Senate Democratic leadership team, which is not mentioned in the premise
if hypothesis_warren_joined_senate_democratic_leadership_team:
    label = "entailment"
else:
    label = "neutral"

print(label)
