library(visNetwork)
library(networkD3)
library(igraph)
# 节点数据集: 共包含三列，依次是起点、终点、边的粗细(大小、权重)
data(MisLinks)
# 边数据集: 共包含三列，节点名称，节点分组，节点大小(重要性、集中度)。
# 用节点的ID来代替节点本身，networkD3包是从0开始编号的
data(MisNodes)
# 鼠标点击事件（弹出节点描述）
# clickJS <- "
# d3.selectAll('.xtooltip').remove(); 
# d3.select('body').append('div')
# .attr('class', 'xtooltip')
# .style('position', 'fixed')             # 描述出现位置
# .style('border-radius', '0px')
# .style('padding', '5px')
# .style('opacity', '0.85')              
# .style('background-color', '#161823')
# .style('box-shadow', '2px 2px 6px #161823')
# # 描述内容
# .html('name: ' + d.description + '<br>' + 'group: ' + d.group) 
# .style('right', '50px')
# .style('bottom', '50px')
# # 描述颜色
# .style('color', d3.select(this).style('fill'))
# ;
# "
# 边颜色
# Cols <- car::recode(edges$weight,"1:6='#A78E44'")
forceNetwork(Links = MisLinks,             # 边数据
                   Nodes = MisNodes,       # 节点数据
                   Source = "source",      # 起始点
                   Target = "target",      # 终点
                   NodeID = "name",        # 节点名称
                   Group = "group",        # 节点分组
                   Value = "value",        # 边粗细  
                   fontFamily = "黑体",    # 字体 
                   opacity = 1,            # 透明度
                   fontSize = 16,          # 字号
                   zoom = T,               # 是否缩放
                   charge=-50,             # 节点斥力大小（负值越大斥力越大）
                   bounded=T,              # 是否有边界
                   legend=T,               # 是否显示图例
                   arrows = F,             # 是否显示箭头
                   Nodesize = "size",      # 节点比例
                   # linkColour = Cols,      # 边颜色
                   opacityNoHover = 1,     # 鼠标悬停时透明度
                   radiusCalculation = JS(" d.nodesize"),      # 节点大小
                   # ColourScale <- 'd3.scaleOrdinal()           # 节点颜色
                   # .domain(["顾", "世家"])
                   # .range(["#FF6900", "#694489"]);',
                   width = 1200,          # 图宽度                  
                   height = 500,          # 图高度
                   # clickAction= clickJS   # 鼠标点击事件
)

