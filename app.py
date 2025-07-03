'''
f = open("r.txt",'r')
lines = f.readline()
for line in lines:
    print(line.strip())
f.close
f = open("output.txt","w")
f.write("""Hello World!
Yo! Whats Good Hommie...
Havin' Fun.""")
f.close()
f = open("output.txt","a")
f.write("""\nHello World!
Yo! Whats Good Hommie...
Havin' Fun.""")
f.close()'''
