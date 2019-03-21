var xValues9 = document.querySelector('#my_variable_x33').value.split(" ")
var yValues9 = document.querySelector('#my_variable_y33').value.split(" ")

var thisYear = new Date().getFullYear()


var data9 = [{
  x: xValues9,
  y: yValues9,
  type: 'bar',
  textposition: 'auto',
  hoverinfo: "Weekly Octave Sum: "+yValues8.map(String)+", Week of the Year: "+xValues8.map(String),
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
      text: '<b>2018</b>',
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
    tickmode: 'auto',
    nticks: 4,
    range: [thisYear+'-01-01 12:00', thisYear+'-12-31 12:00'], 
    rangeslider: {range: [thisYear+'-01-01 12:00', thisYear+'-12-31 12:00']}, 
    title: 'Week of the Year', },

    yaxis: {
      linecolor: 'black',
      linewidth: 2,
      mirror: true
    }
};

Plotly.newPlot('OctavesDiv3', data9, layout);





