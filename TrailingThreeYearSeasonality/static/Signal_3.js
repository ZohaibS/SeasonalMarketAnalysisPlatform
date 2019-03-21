var xValues6 = document.querySelector('#my_variable_x23').value.split(" ")
var yValues6 = document.querySelector('#my_variable_y23').value.split(" ")

var thisYear = new Date().getFullYear()

var data6 = [
    {
    x: xValues6,
    y: yValues6,
    fill: 'tozeroy',
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
      text: '<b>2018</b>',
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


Plotly.newPlot('SignalDiv3', data6, layout);





