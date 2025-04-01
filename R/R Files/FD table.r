 grades <- c(62, 87, 81, 69, 87, 62, 45, 95, 76, 76, 62, 71, 65, 67, 72, 80, 40, 77, 87, 58,
            84, 73, 93, 64, 89)
class_limits<-c(40,50,60,70,80,90,100)
freq_table<-table(cut(grades, breaks=class_limits, right=FALSE))
midpoints<-(class_limits[-1]+class_limits[-length(class_limits)])/2
rel_freq<-prop.table(freq_table)
cum_freq<-cumsum(freq_table)
k<-diff(class_limits)[1]
print("Table:")
result_table<-data.frame(Class_limit=paste("[",class_limits[-length(class_limits)],
                                           "-",class_limits[-1],")", sep=""),
                         Frequency=as.vector(freq_table),
                         Relative_Frequency=as.vector(rel_freq),
                         Cumulative_Frequency=cum_freq,
                         Midpoints=midpoints)
print(result_table)