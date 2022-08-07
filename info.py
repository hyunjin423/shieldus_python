
infilename = input("입력 파일 이름: ");
outfilename = input("출력 파일 이름: ");

infile = open(infilename, "r")
outfile = open(outfilename, "w")

#매출 합계, 평균내기 위한 count
sum = 0
count = 0

line = infile.readline()
while line != "" :
	s = int(line)
	sum += s
	count += 1
	line = infile.readline()

#나중에 출력할 때 사용..
outfile.write("총매출 = "+ str(sum)+"\n")
outfile.write("평균 일매출 = "+ str(sum/count ))

infile.close() 
outfile.close()
