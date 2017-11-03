<template>
  <div style="width:100%;height:100%;position:absolute;">
    <div style="padding:2em;">
      <div style="margin:0 auto 2em auto;">
        <div style="display:flex;justify-content:space-evenly;">
          <div style="display:flex;justify-content:center;flex-direction:column;">Control Panel: </div>
          <div>
            <div>
              <span>X-Axis:</span>
              <el-select style="max-width:10em;" @change="updateGraph" v-model="selectedColumn" placeholder="select predictor">
                <el-option v-for="(item,index) in labels" :key="index" :label="item" :value="item">
                </el-option>
              </el-select>
              <span>Leaf node:</span>
              <el-select style="max-width:5em;" @change="updateGraph" v-model="leafNode" placeholder="select leaf node">
                <el-option label="all" :value="-1">
                </el-option>
                <el-option v-for="(item,index) in allLeaf" :key="index" :label="item" :value="item">
                </el-option>
              </el-select>
              <el-date-picker v-model="startYear" type="year" @change="updateGraph" placeholder="Starting year">
              </el-date-picker>
              <el-date-picker v-model="endYear" type="year" @change="updateGraph" placeholder="Ending year">
              </el-date-picker>
            </div>
            <div style="margin-top:0.5em;">
              <el-checkbox @change="updateGraph" v-model="drawLoess">LOESS</el-checkbox>
              <el-checkbox @change="updateGraph" v-model="jitterThem">Jitter</el-checkbox>
              <el-checkbox @change="updateGraph" v-model="excludeZero">Exclude 0</el-checkbox>
            </div>
          </div>
          <div>
            <el-button @click="forkGraph">Fork</el-button>
            <el-button @click="cutGraph">Cut</el-button>
          </div>
        </div>
      </div>
      <div v-loading.body="showLoading" id='nhldata' style="min-width:400px;min-height:400px;">
      </div>
    </div>
    <div style="display:flex; flex-wrap:wrap;justify-content:space-around;">
      <div style="width:500px;height:300px;" :id="'fork'+index" v-for="(item,index) in allForks" :key="index"></div>
    </div>
  </div>
</template>

<script>
// import loess from '../assets/loess.js'
import science from 'science'
import echarts from 'echarts'
import playerRawData from '../assets/joined_leaf_node.csv'
const INDEX_Y = 20
const INDEX_YEAR = 19
// const INDEX_NAME = 1
const INDEX_LEAF = 18
let JITTERCONST = 50
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
      leafNode: 1,
      allLeaf: [1, 2, 3, 4, 5, 6, 7],
      currentOption: '',
      allForks: [],
      showLoading: true,
      drawLoess: true,
      excludeZero: false,
      jitterThem: true
    }
  },
  mounted() {
    this.myChart = echarts.init(document.getElementById('nhldata'))
    this.labels = playerRawData[0]
    this.allData = playerRawData.slice(1)
    let self = this
    self.showLoading = true
    setTimeout(function() {
      self.updateGraph()
      self.showLoading = false
    }, 2000)
  },
  methods: {
    drawPlot: function(scatterData, loessData) {
      let self = this
      self.currentOption = {
        title: {
          text: 'sum_7yr_GP vs ' + self.selectedColumn + ' (leaf: ' + (self.leafNode === -1 ? 'all' : self.leafNode) + ')',
          left: 'center'
        },
        xAxis: {
          name: self.selectedColumn,
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
          name: 'sum_7yr_GP',
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
          data: scatterData,
          type: 'scatter',
          label: {
            emphasis: {
              show: true,
              formatter: param => param.data[2],
              position: 'top'
            }
          }
        }, {
          data: loessData,
          type: 'line',
          smooth: true,
          showSymbol: false
        }]
      }
      this.myChart.setOption(self.currentOption)
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
      cleanData = cleanData.map(item => [parseInt(item[columnIndex]), parseInt(item[INDEX_Y])])

      if (self.excludeZero) {
        cleanData = cleanData.filter(item => {
          return item[1] !== 0
        })
      }
      let loessData = []
      if (self.drawLoess) {
        let loessPlot = cleanData.sort((a, b) => a[0] - b[0])
        if (self.jitterThem) {
          let xAxisValues = cleanData.map(item => item[0])
          let maxX = Math.max(...xAxisValues)
          let minX = Math.min(...xAxisValues)
          let jitterValue = (maxX - minX) / JITTERCONST
          loessPlot = loessPlot.map((item, index, self) => {
            if (self[index + 1] && Math.abs(item[0] - self[index + 1][0]) < jitterValue) {
              item[0] += Math.random() * jitterValue - jitterValue / 2
              return item
            } else {
              return item
            }
          }).sort((a, b) => a[0] - b[0])
        }
        let cleanX = loessPlot.map(item => item[0])
        let cleanY = loessPlot.map(item => item[1])
        let loessF = science.stats.loess().bandwidth(0.2)
        loessData = loessF(cleanX, cleanY).filter(item => item)
        loessData = loessData.map((item, i) => [cleanX[i], item])
      }
      this.drawPlot(cleanData, loessData)
    },
    forkGraph: function() {
      let self = this
      this.allForks.push(this.currentOption)
      this.$nextTick(function() {
        let dom = document.getElementById('fork' + (self.allForks.length - 1))
        let smallChart = echarts.init(dom)
        smallChart.setOption(this.currentOption)
      })
    },
    cutGraph: function() {
      this.allForks.pop()
    }
  }
}
</script>

<!-- Add 'scoped' attribute to limit CSS to this component only -->
<style scoped>

</style>
