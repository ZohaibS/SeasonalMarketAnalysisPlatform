var xValues7 = document.querySelector('#my_variable_x31').value.split(" ")
var yValues7 = document.querySelector('#my_variable_y31').value.split(" ")

var thisYear = new Date().getFullYear()


var data7 = [{
  x: xValues7,
  y: yValues7,
  type: 'bar',
  textposition: 'auto',
  hoverinfo: "Weekly Octave Sum: "+yValues7.map(String)+", Week of the Year: "+xValues7.map(String),
  marker: {
    color: 'rgb(158,202,225)',
    opacity: 0.7,
    line: {
      color: 'rgb(8,48,107)',
      width: 1.5
    }
  }
}];


var layout = {
  autosize: false,
  width: 450,
  height: 600,
  margin: {
    b: 100,
    l: 50
  },
  title: {
      text: '<b>2016</b>',
      font: {
        family: 'Garamond, serif',
        size: 30,
        color: 'black'
      }},
      
  xaxis: {          
    linecolor: 'black',
    linewidth: 2,
    mirror: true,
    domain: [0, 1], 
    range: [thisYear+'-01-01 12:00', thisYear+'-12-31 12:00'], 
    rangeslider: {range: [thisYear+'-01-01 12:00', thisYear+'-12-31 12:00']}, 
    title: 'Week of the Year', },
    yaxis: {
      title: {
        text: '<b>Sum of Octaves Over the Week</b>',
        font: {
          family: 'Garamond, serif',
          size: 18,
          color: 'black'
        }
      },
      linecolor: 'black',
      linewidth: 2,
      mirror: true
    }
};

Plotly.newPlot('OctavesDiv1', data7, layout);





