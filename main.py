import string
f = open('combatlog.txt')
f = f.read().split("")
i = 0
for item in f:
    s = f[i]
    s = s[0:-2].strip()
    k = s[0:9]
    k = k.strip()
    if k == "type: 4":
        if "is_target_hero: 1" in s:
            print(s[9:38].strip())
    i += 1