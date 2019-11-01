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
    success: function (data, status) { globalObject = data; },
    timeout: 2500 // this should be a pretty sane timeout
  }).done(
    document.write(globalObject)
  ) // INSERT THE DATA HANDLER HERE!!!

function fillTable (obj, dom) {
  // applies data in obj[0] to HTML tags with the obj's key as ID.
  // useful mostly for slapping spectrometer JSON into HTML tables.
  for (var i in obj[0]) {
    $(dom).find('#' + i).text(obj[0][i]);
  }
}

function graphSpectralData (obj, dom) {
  // graphs the data from obj[0] into canvas at dom
  var arr = [];
  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'R', 'I', 'S', 'J', 'T', 'U', 'V', 'W', 'K', 'L'].forEach(function (i) {
    arr.push(obj[0][i]);
  })
}

function fillLuxUv (obj, dom) {
  $(dom).find('#lx').text(obj[1]);
  $(dom).find('#uva').text(obj[2][0]);
  $(dom).find('#uvb').text(obj[2][1]);
  $(dom).find('#uvi').text(obj[2][2]);
}
