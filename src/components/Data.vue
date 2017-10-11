<template>
  <div style="width:100%;height:100%;position:absolute;">
    <div style="padding:2em;">
      <div style="margin:0 auto 2em auto;">
        <div style="display:flex;justify-content:space-evenly;">
          <div style="display:flex;justify-content:center;flex-direction:column;">Control Panel: </div>
          <el-select @change="updateGraph" v-model="selectedColumn" placeholder="select predictor">
            <el-option v-for="(item,index) in labels" :key="index" :label="item" :value="item">
            </el-option>
          </el-select>
          <el-select @change="updateGraph" v-model="leafNode" placeholder="select leaf node">
            <el-option label="all" :value="-1">
            </el-option>
            <el-option v-for="(item,index) in allLeaf" :key="index" :label="item" :value="item">
            </el-option>
          </el-select>
          <el-date-picker v-model="startYear" type="year" @change="updateGraph" placeholder="Starting year">
          </el-date-picker>
          <el-date-picker v-model="endYear" type="year" @change="updateGraph" placeholder="Ending year">
          </el-date-picker>
          <el-button @click="updateGraph">Refresh</el-button>
        </div>
      </div>
      <div id='nhldata' style="min-width:400px;min-height:400px;">
      </div>
    </div>
  </div>
</template>

<script>
import echarts from 'echarts'
import playerRawData from '../assets/joined_leaf_node.csv'
const INDEX_Y = 11
const INDEX_YEAR = 5
const INDEX_NAME = 1
const INDEX_LEAF = 10
export default {
  name: 'template',
  data() {
    return {
      myChart: '',
      labels: '',
      allData: '',
      plotData: [],
      selectedColumn: 'Weight',
      startYear: new Date(2004, 1, 1),
      endYear: new Date(2008, 1, 1),
      leafNode: -1,
      allLeaf: [1, 2, 3, 4, 5, 6, 7]
    }
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById('nhldata'))
    this.labels = playerRawData[0]
    this.allData = playerRawData.slice(1)
    this.$message('Large dataset may slow down your computer, Chrome is recommended.')
  },
  methods: {
    drawPlot: function(plotData) {
      let self = this
      this.myChart.setOption({
        title: {
          text: 'sum_7yr_GP vs ' + self.selectedColumn,
          left: 'center'
        },
        xAxis: {
          name: self.selectedColumn,
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          },
          scale: true
        },
        yAxis: {
          name: 'sum_7yr_GP',
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          },
          scale: true
        },
        tooltip: {
          showDelay: 0,
          axisPointer: {
            show: true,
            type: 'cross',
            lineStyle: {
              type: 'dashed',
              width: 1
            }
          }
        },
        series: [{
          data: plotData,
          type: 'scatter',
          label: {
            emphasis: {
              show: true,
              formatter: param => param.data[2],
              position: 'top'
            }
          }
        }]
      })
    },
    updateGraph: function() {
      let self = this
      let start = this.startYear.getFullYear()
      let end = this.endYear.getFullYear()
      let columnIndex = this.labels.indexOf(this.selectedColumn)

      let cleanData = this.allData.filter(item => {
        return parseInt(item[INDEX_YEAR]) >= start && parseInt(item[INDEX_YEAR]) <= end
      })
      if (self.leafNode !== -1) {
        cleanData = cleanData.filter(item => parseInt(item[INDEX_LEAF]) === self.leafNode)
      }
      cleanData = cleanData.map(item => [item[columnIndex], item[INDEX_Y], item[INDEX_NAME]])
      this.drawPlot(cleanData)
    }
  }
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>

</style>
