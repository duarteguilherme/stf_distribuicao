library(dplyr)
library(tidyr)
library(readr)

sites <- read_csv('sites.csv')

sites <- filter(sites, site!="N")


write_csv(sites, "sites.csv")
