<template>
  <div class="hello">
    <div>
      <el-input  style="max-width:20em;" v-model="userURL"></el-input>
      <el-button @click="getDataFromURL">Get data</el-button> 
      <el-upload :on-change="getDataFromUpload" action="#" :auto-upload="false">
        <el-button>click to upload data</el-button>
      </el-upload>  
    </div>     
    <el-select @change="updateConfig" v-model="xAxis">
      <el-option v-for="(item,index) in csvColumns" :key="index" :label="item" :value="item" placeholder="x Axis"></el-option>
    </el-select>
    <el-select @change="updateConfig" v-model="yAxis">
      <el-option v-for="(item,index) in csvColumns" :key="index" :label="item" :value="item" placeholder="y Axis"></el-option>
    </el-select>
     <el-checkbox @change="updateConfig" v-model="loess">Show loess</el-checkbox>
    <div id='data' style="min-width:400px;min-height:400px;">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import science from 'science'
import echarts from 'echarts'
export default {
  name: 'general',
  data() {
    return {
      msg: 'Welcome to Your Vue.js PWA',
      csvColumns: [],
      csvData: [],
      xAxis: '',
      yAxis: '',
      dataChart: '',
      fileContent: '',
      loess: true,
      loessData: [],
      mainPlotData: '',
      userURL: 'https://file.haoxp.xyz/players.csv'
    }
  },
  mounted() {
    this.dataChart = echarts.init(document.getElementById('data'))
  },
  methods: {
    dataPipeLine: function (rawData) {
      // rawData looks like: [[x1, y1], [x2, y2]...]
      let self = this
      if (self.loess) {
        let loessData = rawData.sort((a, b) => a[0] - b[0])
        let xValues = loessData.map(item => item[0])
        let yValues = loessData.map(item => item[1])
        let loessF = science.stats.loess().bandwidth(0.2)
        loessData = loessF(xValues, yValues)
        loessData = loessData.map((item, i) => [xValues[i], item])
        self.loessData = loessData
      } else {
        self.loessData = []
      }
      self.mainPlotData = rawData
    },
    getDataFromUpload: function (file) {
      let self = this
      let reader = new FileReader()
      reader.onload = e => {
        self.dispatchData(self.csvToArray(e.target.result))
      }
      reader.readAsText(file.raw)
    },
    getDataFromURL: function () {
      let self = this
      axios.get(self.userURL)
        .then(response => {
          let parsedCSV = self.csvToArray(response.data)
          self.dispatchData(parsedCSV)
        })
    },
    dispatchData: function (rawCSVData) {
      this.csvColumns = rawCSVData[0]
      this.csvData = rawCSVData.slice(1, -1)
      this.xAxis = ''
      this.yAxis = ''
    },
    drawPlot: function () {
      let self = this
      let options = {
        title: {
          text: self.yAxis + ' vs ' + self.xAxis,
          left: 'center'
        },
        xAxis: {
          name: self.xAxis,
          nameLocation: 'middle',
          nameGap: 20,
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          },
          scale: true
        },
        yAxis: {
          name: self.yAxis,
          splitLine: {
            lineStyle: {
              type: 'dashed'
            }
          },
          scale: false
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
          data: self.mainPlotData,
          type: 'scatter',
          label: {
            emphasis: {
              show: true,
              formatter: param => param.data[2],
              position: 'top'
            }
          }
        }, {
          data: self.loessData,
          type: 'line',
          smooth: true,
          showSymbol: false
        }]
      }
      this.dataChart.setOption(options)
    },
    updateConfig: function () {
      let xIndex = this.csvColumns.indexOf(this.xAxis)
      let yIndex = this.csvColumns.indexOf(this.yAxis)
      if (xIndex < 0 || yIndex < 0) return
      let plotData = this.csvData.map(item => {
        return [item[xIndex], item[yIndex]]
      })
      console.log(plotData)
      this.dataPipeLine(plotData)
      this.drawPlot()
    },
    csvToArray: function (text) {
      let p = ''
      let row = ['']
      let ret = [row]
      let i = 0
      let r = 0
      let s = !0
      let l
      for (l in text) {
        l = text[l]
        if (l === '"') {
          if (s && l === p) row[i] += l
          s = !s
        } else if (l === ',' && s) l = row[++i] = ''
        else if (l === '\n' && s) {
          if (p === '\r') row[i] = row[i].slice(0, -1)
          row = ret[++r] = [l = '']
          i = 0
        } else row[i] += l
        p = l
      }
      return ret
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #35495e;
}
</style>
