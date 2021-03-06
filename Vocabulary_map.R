# install.packages('readr') 
# install.packages('tidyverse')
library(visNetwork)
library(networkD3)
library(igraph)
# library(tidyverse)
# library(stringr)
# library(readr)
# library(dplyr)
# library(tibble)
# library(reshape2)
vocabulary<-data.frame(read.csv("/home/skylark/PycharmRemote/Vocabulary_Analysis/IELTS_vocabulary_sorted/01��ѧ�Ʒ��ࣺ����.csv",
                                fileEncoding = "GBK",  #ָ���ļ��ı���
                                encoding = "GBK",  #ָ������
                                       header = FALSE))
# --------- Easy version ------
# Create data
# src <- c(rep('Weather',48))
# target <- vocabulary$V2
# 
# networkData <- data.frame(src, target)
# 
# # Plot
# simpleNetwork(networkData)
# ----------------------------
source <- c(rep(0,4), rep(3,14), rep(7,10), rep(29,10), rep(31,10))
target <- vocabulary$V1
value <- rep(1,48)
MisLinks <- data.frame(source, target, value)
name <- c('Weather', as.character(vocabulary$V2))
group<-rep(1, 49)
size<-rep(10, 49)
description <- c('Weather', as.character(vocabulary$V3))
class <- unlist(lapply(description, FUN = function(x) {return(strsplit(x, split = ". ")[[1]][1])}))

for (i in seq_along(class)) {               #2.������
  if(class[i] == 'n'){
    group[i]=2
  }
  else if(class[i] == 'adj'){
    group[i]=3
  }
  else if (class[i] == 'v'){
    group[i]=4
  }
  else if (class[i] == 'vt'){
    group[i]=5
  }
  else if (class[i] == 'adv'){
    group[i]=6
  }
  else if (class[i] == 'vi'){
    group[i]=7
  }
  else {
    group[i]=1
  }
}

MisNodes <- data.frame(name, group, size, description, class)

# ������¼��������ڵ�������
# clickJS <- "
# d3.selectAll('.xtooltip').remove();
# d3.select('body').append('div')
#   .attr('class', 'xtooltip')
#   .style('position', 'fixed')             # ��������λ��
#   .style('border-radius', '0px')
#   .style('padding', '5px')
#   .style('opacity', '0.85')
#   .style('background-color', '#161823')
#   .style('box-shadow', '2px 2px 6px #161823')
# # ��������
#   .html('name: ' + d.description + '<br>' + 'group: ' + d.group)
#   .style('right', '50px')
#   .style('bottom', '50px')
# # ������ɫ
#   .style('color', d3.select(this).style('fill'));
# "
script <- 'alert("Meaning: " + (d.description));'

fn <- forceNetwork(Links = MisLinks,       # 边数�?
                   Nodes = MisNodes,       # 节点数据
                   Source = "source",      # 起始�?
                   Target = "target",      # 终点
                   NodeID = "name",        # 节点名称
                   Group = "group",        # 节点分组
                   Value = "value",        # 边粗�?  
                   fontFamily = "����",    # 字体 
                   opacity = 1,            # 透明�?
                   fontSize = 16,          # 字号
                   zoom = T,               # 是否缩放
                   charge=-50,             # 节点斥力大小（负值越大斥力越大）
                   bounded=T,              # 是否有边�?
                   legend=T,               # 是否显示图例
                   arrows = F,             # 是否显示箭头
                   Nodesize = "size",      # 节点比例
                   # linkColour = Cols,      # 边颜�?
                   opacityNoHover = 1,     # 鼠标悬停时�?�明�?
                   radiusCalculation = JS(" d.nodesize"),      # 节点大小
                   # ColourScale <- 'd3.scaleOrdinal()           # 节点颜色
                   # .domain(["�?", "世家"])
                   # .range(["#FF6900", "#694489"]);',
                   width = 1200,          # 图宽�?                  
                   height = 500,          # 图高�?
                   clickAction= script   # 鼠标点击事件
)
fn$x$nodes$description <- MisNodes$description
fn
saveNetwork(fn, '/home/skylark/PycharmRemote/Vocabulary_Analysis/net5.html')
  