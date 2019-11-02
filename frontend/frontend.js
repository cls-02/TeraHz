// All code in this file is licensed under the ISC license, provided in LICENSE.txt
$('#update').click(function () {
  updateData();
});
// jQuery event binder

function updateData () {
  const url = 'http://' + window.location.hostname + ':5000/data';
  $.ajax({ // spawn an AJAX request
    url: url,
    success: function (data, status) {
      console.log(data);
      graphSpectralData(data[0], 0);
      fillTableData(data);
    },
    timeout: 2500 // this should be a pretty sane timeout
  });
}

function graphSpectralData (obj, dom) {
  // graph spectral data in obj into dom
  var graphPoints = [];
  Object.keys(obj).forEach((element, index) => {
    graphPoints.push([index, obj[element]]);
  });
  console.log(graphPoints);
  const options = {
    color: 'white',
    grid: {
      color: 'white'
    },
    xaxis: {
      color: 'green'
    },
    yaxis: {
      color: 'blue'
    }
  };
  $.plot('#graph', [graphPoints], options);
  // flot expects an array of arrays (lines) of 2-element arrays (points)
}

function fillTableData (obj) {
  // fill the obj data into HTML tables
  Object.keys(obj[0])
    .forEach((element) => { $('#' + element).text(obj[0][element]); });
  $('#lx').text(obj[1]);
  $('#uva').text(obj[2][0]);
  $('#uvb').text(obj[2][1]);
  $('#uvi').text(obj[2][2]);
}
