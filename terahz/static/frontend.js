// All code in this file is licensed under the ISC license, provided in LICENSE.txt
$('#update').click(updateData);
// jQuery event binder

function updateData () {
const url = '/data';
  $.get(url, (data, status) => {
    if (status === '200') {
      graphSpectralData(data[0], 0);
      fillTableData(data);
    } else alert('Data request failed, please refresh page.');
  });
}

function graphSpectralData (obj, dom) {
  // graph spectral data in obj into dom
  var graphPoints = [];
  var graphXTicks = [];

  const spectrum = 'ABCDEFGHRISJTUVWKL';
  for (var i = 0; i < spectrum.length; i++) {
    graphPoints.push([i, obj[spectrum[i]]]);
    graphXTicks.push([i, spectrum[i]]);
  }
  const options = {
    grid: { color: 'white' },
    xaxis: { ticks: graphXTicks }
  };
  $.plot('#graph', [graphPoints], options);
  // flot expects an array of arrays (lines) of 2-element arrays (points)
}

function fillTableData (obj) {
  // fill the obj data into HTML tables
  Object.keys(obj[0])
    .forEach((element) => { $('#' + element + '_value').text(obj[0][element]); });
  $('#lx').text(obj[1]);
  $('#uva').text(obj[2][0]);
  $('#uvb').text(obj[2][1]);
  $('#uvi').text(obj[2][2]);
}
