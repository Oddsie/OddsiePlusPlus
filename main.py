from subprocess import run as shell
from sys import argv as args
def transpile(name):
	f=open(name)
	o=open(name.replace(".opp",".py"),"w")
	olines=[]
	tcount=0
	for line in f:
		dent=""
		line=line.replace("\n","").replace("\t","")
		if line.startswith("class "):
				for i in range(tcount):dent=dent+"\t"
				olines.append(dent+line.replace(" (",":"))
		elif line.startswith("function "):
				for i in range(tcount):dent=dent+"\t"
				edit=line.replace("function ","").replace(" (","").replace("::","-").split("-")
				olines.append(dent+"def "+edit[0]+"("+edit[1]+"):")
		elif line.startswith("var "):
				for i in range(tcount):dent=dent+"\t"
				edit=line.replace("var ","")
				olines.append(dent+edit)
		elif line.startswith("display "):
				for i in range(tcount):dent=dent+"\t"
				edit=line.replace("display ","")
				olines.append(dent+"print("+edit+")")
		elif line.startswith("."):
				for i in range(tcount):dent=dent+"\t"
				edit=line.replace(".","",1).replace("::","-",1).split("-")
				olines.append(dent+edit[0]+"("+edit[1]+")")
		elif line.startswith(";;"):
				pass
		elif line.startswith("use "):
				edit=line.replace("use ","import ",1)
				olines.append(edit)
		elif line=="die":
				print(str(tcount))
				for i in range(tcount):dent=dent+"\t"
				olines.append(dent+"quit()")
		elif line.startswith("if "):
				for i in range(tcount):dent=dent+"\t"
				olines.append(dent+line.replace(" (",":"))
		elif line.startswith("if otherwise"):
				for i in range(tcount):dent=dent+"\t"
				edit=line.replace("if otherwise ","elif ",1).replace(" (",":")
				olines.append(dent+edit)
		elif line.startswith("otherwise "):
				for i in range(tcount):dent=dent+"\t"
				edit=line.replace("otherwise ","else ",1).replace(" (",":") 
				olines.append(dent+edit)
		if line.endswith(" ("):
				tcount+=1
		if line.endswith(" )"):
				tcount-=1
	for item in olines:
		o.write(item+"\n")
	o.write("if __name__=='__main__':\n\tmain=main()")
	return o.name
shell("python3 "+transpile(args[1]),shell=True)
