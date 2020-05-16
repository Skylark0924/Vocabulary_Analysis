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
vocabulary<-data.frame(read.csv("/home/skylark/PycharmRemote/Vocabulary_Analysis/IELTS_vocabulary_sorted/01°´Ñ§¿Æ·ÖÀà£ºÆøÏó.csv",
                                fileEncoding = "GBK",  #Ö¸¶¨ÎÄ¼şµÄ±àÂë
                                encoding = "GBK",  #Ö¸¶¨±àÂë
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

for (i in seq_along(class)) {               #2.µü´úÆ÷
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

# Êó±êµã»÷ÊÂ¼ş£¨µ¯³ö½ÚµãÃèÊö£©
# clickJS <- "
# d3.selectAll('.xtooltip').remove();
# d3.select('body').append('div')
#   .attr('class', 'xtooltip')
#   .style('position', 'fixed')             # ÃèÊö³öÏÖÎ»ÖÃ
#   .style('border-radius', '0px')
#   .style('padding', '5px')
#   .style('opacity', '0.85')
#   .style('background-color', '#161823')
#   .style('box-shadow', '2px 2px 6px #161823')
# # ÃèÊöÄÚÈİ
#   .html('name: ' + d.description + '<br>' + 'group: ' + d.group)
#   .style('right', '50px')
#   .style('bottom', '50px')
# # ÃèÊöÑÕÉ«
#   .style('color', d3.select(this).style('fill'));
# "
script <- 'alert("Meaning: " + (d.description));'

fn <- forceNetwork(Links = MisLinks,       # è¾¹æ•°æ?
                   Nodes = MisNodes,       # èŠ‚ç‚¹æ•°æ®
                   Source = "source",      # èµ·å§‹ç‚?
                   Target = "target",      # ç»ˆç‚¹
                   NodeID = "name",        # èŠ‚ç‚¹åç§°
                   Group = "group",        # èŠ‚ç‚¹åˆ†ç»„
                   Value = "value",        # è¾¹ç²—ç»?  
                   fontFamily = "ºÚÌå",    # å­—ä½“ 
                   opacity = 1,            # é€æ˜åº?
                   fontSize = 16,          # å­—å·
                   zoom = T,               # æ˜¯å¦ç¼©æ”¾
                   charge=-50,             # èŠ‚ç‚¹æ–¥åŠ›å¤§å°ï¼ˆè´Ÿå€¼è¶Šå¤§æ–¥åŠ›è¶Šå¤§ï¼‰
                   bounded=T,              # æ˜¯å¦æœ‰è¾¹ç•?
                   legend=T,               # æ˜¯å¦æ˜¾ç¤ºå›¾ä¾‹
                   arrows = F,             # æ˜¯å¦æ˜¾ç¤ºç®­å¤´
                   Nodesize = "size",      # èŠ‚ç‚¹æ¯”ä¾‹
                   # linkColour = Cols,      # è¾¹é¢œè‰?
                   opacityNoHover = 1,     # é¼ æ ‡æ‚¬åœæ—¶é?æ˜åº?
                   radiusCalculation = JS(" d.nodesize"),      # èŠ‚ç‚¹å¤§å°
                   # ColourScale <- 'd3.scaleOrdinal()           # èŠ‚ç‚¹é¢œè‰²
                   # .domain(["é¡?", "ä¸–å®¶"])
                   # .range(["#FF6900", "#694489"]);',
                   width = 1200,          # å›¾å®½åº?                  
                   height = 500,          # å›¾é«˜åº?
                   clickAction= script   # é¼ æ ‡ç‚¹å‡»äº‹ä»¶
)
fn$x$nodes$description <- MisNodes$description
fn
saveNetwork(fn, '/home/skylark/PycharmRemote/Vocabulary_Analysis/net5.html')
  