import string
s=input('Please enter something:')

count_en = count_dg = count_sp = count_zh = count_pu = 0
s_len = len(s)

for c in s:
    if c in string.ascii_letters:
        count_en += 1
    elif c.isdigit():
        count_dg += 1
    elif c.isspace():
        count_sp += 1
    elif c.isalpha():
        count_zh += 1
    else:
        count_pu += 1
total_chars = count_zh + count_en + count_sp + count_dg + count_pu
if total_chars == s_len:
    pass
else:
    print('Something went wrong! The program ends.')
    exit()

print('该字符串共有 {} 个字符，其中有 {} 个汉字，{} 个英文，{} 个空格，{} 个数字，{} 个其他符号。\
    '.format(total_chars, count_zh, count_en, count_sp, count_dg, count_pu))
