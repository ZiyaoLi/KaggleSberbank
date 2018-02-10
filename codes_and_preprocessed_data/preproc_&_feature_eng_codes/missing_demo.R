library(data.table)
library(tidyverse)
library(lubridate)
library(scales)
library(corrplot)
library(DT)
library(easyGgplot2)

dhouse <- fread('..\\total_mod_split.csv', stringsAsFactors=TRUE)

miss_house <- map_dbl(dhouse, function(x) { round((sum(is.na(x)) / length(x)) * 100, 1) })

miss_house <- miss_house[miss_house > 0]

draion <- fread('..\\raions_raw.csv', stringsAsFactors=TRUE)

miss_raion <- map_dbl(draion, function(x) { round((sum(is.na(x)) / length(x)) * 100, 1) })

miss_raion <- miss_raion[miss_raion > 0]

dmacro <- fread('..\\macro.csv', stringsAsFactors=TRUE)

miss_macro <- map_dbl(dmacro, function(x) { round((sum(is.na(x)) / length(x)) * 100, 1) })

miss_macro <- miss_macro[miss_macro > 0]

p1 = data.frame(miss=miss_house, var=names(miss_house), row.names=NULL) %>%
  ggplot(aes(x=reorder(var, -miss), y=miss)) + 
  geom_bar(stat='identity', fill='red') +
  labs(x='', y='% missing', title='Percent missing data by feature: house and neighborhood') +
  theme(axis.text.x=element_text(angle=90, hjust=1))

p2 = data.frame(miss=miss_raion, var=names(miss_raion), row.names=NULL) %>%
  ggplot(aes(x=reorder(var, -miss), y=miss)) + 
  geom_bar(stat='identity', fill='red') +
  labs(x='', y='% missing', title='Percent missing data by feature: raions') +
  theme(axis.text.x=element_text(angle=90, hjust=1))

p3 = data.frame(miss=miss_macro, var=names(miss_macro), row.names=NULL) %>%
  ggplot(aes(x=reorder(var, -miss), y=miss)) + 
  geom_bar(stat='identity', fill='red') +
  labs(x='', y='% missing', title='Percent missing data by feature: macro') +
  theme(axis.text.x=element_text(angle=90, hjust=1))

ggplot2.multiplot(p1,p2,p3,cols=1)
