val lines = scala.io.Source.fromFile("inputday2.txt").getLines.toVector
var freq = collection.mutable.Map.empty[Char, Int] //en boksatav, antal förekomster av boksatav

for(i <- lines.indices){
  lines(i).toVector.foreach(c => freq += c -> (freq.getOrElse(c, 0) + 1))
}

//xs(headings.indexOf(heading)) -> (freq.getOrElse(xs(headings.indexOf(heading)),0) + 1)
