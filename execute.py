import sys


L = sys.argv[1:]
for i in range(len(L)):
    L[i] = L[i].replace("_", " ").replace('\\n', '\n').replace('\\t', '\t')
for i in L:
    try:
        exec(i)
    except Exception as err:
        print(f"에러: {err}") 