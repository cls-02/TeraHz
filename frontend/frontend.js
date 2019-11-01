// All code in this file is licensed under the ISC license, provided in LICENSE.txt
var globalObject;
$('#update').click(function () {
  updateData();
});
// jQuery event binder

function updateData () {
  const url = 'http://' + window.location.hostname + ':5000/data';
  $.ajax({ // spawn an AJAX request
    url: url,
    success: function (data, status) { globalObject = data; console.log(data); graphSpectralData(globalObject[0], 0); },
    timeout: 2500 // this should be a pretty sane timeout
  })
}


function graphSpectralData (obj, dom) {
  // graph spectral data in obj into dom
  var graphPoints = [];
  Object.keys(obj).forEach((element, index) => {
    graphPoints.push([index, obj[element]]);
  });
  console.log(graphPoints);
  const options = {
    grid: {
      color: 'white'
    }
  }
  $.plot('#graph', [graphPoints], options);
  // flot expects an array of arrays (lines) of 2-element arrays (points)
}

function fillLuxUv (obj, dom) {
  $(dom).find('#lx').text(obj[1]);
  $(dom).find('#uva').text(obj[2][0]);
  $(dom).find('#uvb').text(obj[2][1]);
  $(dom).find('#uvi').text(obj[2][2]);
}
