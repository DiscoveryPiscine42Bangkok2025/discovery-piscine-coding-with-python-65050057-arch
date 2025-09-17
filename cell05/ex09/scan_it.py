import sys, re
if len(sys.argv) != 3:
 tring = sys.argv[2]
same = re.findall(re.escape(keyword), string)
if same :
    print(len(same))
else:
    print("none")   print("none")
    sys.exit()
keyword = sys.argv[1]
