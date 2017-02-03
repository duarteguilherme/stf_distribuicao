

library(tidyverse)


atas <- read.csv('atas.csv',stringsAsFactors = F)
atas <- filter(atas, ministro!="TOTAL")
atas2016 <- filter(atas, ano==2016)

atas2016_2 <- atas2016 %>%
  group_by(mes) %>%
  mutate(total_mes=sum(mes)) %>%
  ungroup() %>%
  group_by(ministro, mes) %>%
  summarise(porcentagem_ministro = sum(total)/total_mes[1])

total2016 <- atas2016 %>%
  group_by(ministro) %>%
  summarise(parcela_ministro=sum(distribuido)/57198) 