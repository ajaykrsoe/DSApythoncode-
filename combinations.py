def combos(curr, rem, ans):
    if not rem:
        ans.append(curr)
        return
    combos(curr, rem[1:], ans)               # skip  fill with 0
    combos(curr + rem[0], rem[1:], ans)      # take fill with 1 

ans = []
combos("", "ABC", ans)
print(ans)
#each time we need to fill a box with 0/1
