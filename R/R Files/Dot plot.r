grades <- c(62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
            84, 73, 93, 64, 89)
class_limits <- c(40, 50, 60, 70, 80, 90, 100)
freq_table <- table(cut(grades, breaks = class_limits, right = FALSE))
midpoints <- (class_limits[-1] + class_limits[-length(class_limits)]) / 2
plot(midpoints, freq_table, type = "p",col="darkgreen" ,main = "Dot Plot", xlab = "Midpoints",
     ylab = "Frequency")
grid()
