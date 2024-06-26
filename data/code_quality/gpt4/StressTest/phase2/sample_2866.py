gang_members_premise = 41
gang_members_hypothesis = 11

# The hypothesis refers to the number of gang members Kala has, which is also mentioned in the premise
if gang_members_hypothesis >= gang_members_premise:
    # check if the number of gang members in the hypothesis contradicts the estimate of less than 'gang_members_premise'
    label = "contradiction"
elif gang_members_hypothesis < gang_members_premise:
    # the premise gives only an estimate for the number of gang members
    # any number less than 'gang_members_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
