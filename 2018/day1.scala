val lines = scala.io.Source.fromFile(".\\inputday1.txt").getLines.toVector

var sum = 0
for(i <- lines.indices){
  if(lines(i)(0) == '+') sum += lines(i).tail.toInt
  else sum -= lines(i).tail.toInt
}
