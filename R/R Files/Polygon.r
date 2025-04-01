grades <- c(62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
            84, 73, 93, 64, 89)
breaks <- seq(40, 100, by=10)
grades.cut <- cut(grades, breaks, right=FALSE)
grades.freq <- table(grades.cut)
grades.cumfreq <- cumsum(grades.freq)
cumfreq0 <- c(0, grades.cumfreq)
plot(breaks, cumfreq0, type="o",col="blue" ,main="Polygon", xlab="Grades", ylab="Cumulative Frequency")

