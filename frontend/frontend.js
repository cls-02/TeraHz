// All code in this file is licensed under the ISC license, provided in LICENSE.txt
var globalObject;
$('#update').click(function () {
  updateData();
});
// jQuery event binder

function updateData () {
  // download data from backend into obj
  const url = 'http://' + window.location.hostname + ':5000/data';
  // I understand how bad this line looks. Please don't judge me...
  $.get(url, function (data, status) { // standard jQuery AJAX
    globalObject = data;
  })
    .done(function () {
      fillTable(globalObject, $('#specter'));
      graphSpectralData(globalObject, $('#spectrogram'));
      fillLuxUv(globalObject, $('#luxuv'));
    });
}

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
  });
  var chart = new Chart(dom, {
    type: 'line',
    data: {
      labels: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'R', 'I', 'S', 'J', 'T', 'U', 'V', 'W', 'K', 'L'],
      datasets: [{
        label: 'Spectrometer data',
        data: arr
      }]
    },
    options: {
      responsive: false
    }
  });
}

function fillLuxUv (obj, dom) {
  $(dom).find('#lx').text(obj[1]);
  $(dom).find('#uva').text(obj[2][0]);
  $(dom).find('#uvb').text(obj[2][1]);
  $(dom).find('#uvi').text(obj[2][2]);
}
