
def combos(curr, rem, ans):
    if not rem:
        ans.append(curr)
        return
    combos(curr, rem[1:], ans)               # skip
    combos(curr + rem[0], rem[1:], ans)      # take

ans = []
combos("", "ABC", ans)
print(ans)

