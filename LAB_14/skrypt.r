library(magrittr)
# install.packages("ggplot2")
library(ggplot2)
library(dplyr)

# Zadanie 1.1:
list_1 <- 1:10
print(list_1)

# Zadanie 1.2:
list_1%<>%log2()%>%sin()%>%sum()%>%sqrt()
print(list_1)

# Zadanie 1.3:
data(iris)

# Zadanie 1.4:
print(head(iris))

# Zadanie 1.5:
mean_values_all <- iris %>% aggregate(. ~ Species, ., mean)
print(mean_values_all)

# Zadanie 2.1-2.4:
plot_iris1 <- ggplot(iris, aes(x = Sepal.Length)) + 
  geom_histogram(aes(fill = Species), color = "black", alpha = 0.5) + 
  geom_vline(data = mean_values_all, aes(xintercept = Sepal.Length, color =  Species), linetype = "dashed") +
  xlab("Sepal Length") + 
  ylab("Frequency") +
  ggtitle("Iris Dataset Histograms") +
  theme(legend.position = "none")

ggsave("/root/laboratorium_13/plot_iris1.jpg", plot = plot_iris1)

# Zadanie 2.5:
# install.packages("GGally")
library("GGally")

pairs <- ggpairs(data = iris, aes(color = Species))
# Zadanie 2.6:
ggsave("/root/laboratorium_13/plot_iris_pairs.jpg", plot = pairs)


# Zadanie 3.1 i 3.2:
# install.packages("cluster")
library(cluster)

# Zadanie 3.3:
x_iris <- iris[,1:4]
y_iris <- iris[,5]

sum_sqr <- c()

# Zadanie 3.4 i 3.5:
for (i in 1:10){
    result_kmeans <- kmeans(x_iris, i)
    sum_sqr <- append(sum_sqr, result_kmeans$tot.withinss)
}

# Zadanie 3.6:
plot_cluster_1 <- ggplot(data.frame(iteration = 1:length(sum_sqr), value = sum_sqr), aes(x = iteration, y = sum_sqr)) +
                    geom_line()

ggsave("/root/laboratorium_13/plot_cluster_1.jpg", plot = plot_cluster_1)

# Zadanie 3.7:
result_kmeans <- kmeans(x_iris, 3)
plot_cluster_1 <- ggplot(iris, aes(x=Sepal.Length, y=Petal.Length, color=result_kmeans$cluster)) +
                    geom_point()
ggsave("/root/laboratorium_13/plot_cluster_2.jpg", plot = plot_cluster_1)

# Zadanie 3.8:
plot_cluster_1 <- ggplot(iris, aes(x=Sepal.Length, y=Petal.Length, color=Species)) +
                    geom_point()

ggsave("/root/laboratorium_13/plot_cluster_3.jpg", plot = plot_cluster_1)
