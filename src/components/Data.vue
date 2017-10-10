<template>
  <div style="width:100%;height:100%;position:absolute;">
    <div style="padding:2em;">
      <div>Large dataset may slow down your computer, Chrome is recommended.</div>
      <div id='nhldata' style="min-width:400px;min-height:400px;">
      </div>
      <div>
        <div>Control Panel: </div>
        <el-select @change="updateGraph" v-model="selectedColumn" placeholder="select predictor">
          <el-option v-for="(item,index) in labels" :key="index" :label="item" :value="item">
          </el-option>
        </el-select>
        <el-date-picker v-model="startYear" type="year" @change="updateGraph" placeholder="Starting year">
        </el-date-picker>
        <el-date-picker v-model="endYear" type="year" @change="updateGraph" placeholder="Ending year">
        </el-date-picker>
        <el-button @click="updateGraph">Refresh</el-button>
      </div>
    </div>
  </div>
</template>

<script>
import echarts from 'echarts'
import playerRawData from '../assets/joinData.csv'
const INDEX_Y = 22
const INDEX_YEAR = 8
const INDEX_NAME = 1
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
      endYear: new Date(2008, 1, 1)
    }
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById('nhldata'))
    this.labels = playerRawData[0]
    this.allData = playerRawData.slice(1)
  },
  methods: {
    drawPlot: function(plotData) {
      let self = this
      this.myChart.setOption({
        title: { text: 'sum_7yr_GP vs ' + self.selectedColumn },
        xAxis: {
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          },
          scale: true
        },
        yAxis: {
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
      let start = this.startYear.getFullYear()
      let end = this.endYear.getFullYear()
      let columnIndex = this.labels.indexOf(this.selectedColumn)

      let cleanData = this.allData.filter(item => {
        return parseInt(item[INDEX_YEAR]) >= start && parseInt(item[INDEX_YEAR]) <= end
      })
      cleanData = cleanData.map(item => [item[columnIndex], item[INDEX_Y], item[INDEX_NAME]])
      this.drawPlot(cleanData)
    }
  }
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>

</style>
