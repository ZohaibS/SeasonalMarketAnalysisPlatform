var xValues2 = document.querySelector('#my_variable_x12').value.split(" ")
var yValues2 = document.querySelector('#my_variable_y12').value.split(" ")

var thisYear = new Date().getFullYear()

var data2 = [
    {
    x: xValues2,
    y: yValues2,
    type: 'scatter'
    }
];

var layout = {
  autosize: false,
  width: 450,
  height: 600,
  margin: {
    b: 100,
    l: 50
  },
  title: {
      text: '<b>2017</b>',
      font: {
        family: 'Garamond, serif',
        size: 30,
        color: 'black'
      }},
  xaxis : {
      // tickformat: "%D~%M",
      linecolor: 'black',
      linewidth: 2,
      mirror: true,
      title: {
      text: '<b>Date</b>',
      font: {
        family: 'Garamond, serif',
        size: 18,
        color: 'black'
      }},
      tickmode: 'auto',
      nticks: 4,
      tickangle: '15',
      tickfont: {
          family: 'Garamond, serif',
          size: 14,
          color: 'black'
        },
        autorange: true, 
        domain: [0, 1], 
        range: [thisYear+'-01-01 12:00', thisYear+'-12-31 12:00'], 
        rangeslider: {range: [thisYear+'-01-01 12:00', thisYear+'-12-31 12:00']}, 
        title: 'Date', 
   },
   yaxis: {
    linecolor: 'black',
    linewidth: 2,
    mirror: true
  }
};


Plotly.newPlot('myDiv2', data2, layout)


