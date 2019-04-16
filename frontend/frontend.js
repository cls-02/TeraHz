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
      fillTable(globalObject, $('table'));
      graphSpectralData(globalObject, $('#spectrogram'));
    });
}

function fillTable (obj, dom) {
  // applies data in obj[0] to HTML tags with the obj's key as ID.
  // useful mostly for slapping spectrometer JSON into HTML tables.
  for (var i in obj[0]) {
    $(dom).find('#' + i).text(obj[0][i]);
  }
}

function graphSpectralData(obj, dom) {
  // graphs the data from obj[0] into canvas at dom
  var chart = new Chart(dom, {
    type: 'line',
    data: {
      labels: Object.keys(obj[0]),
      datasets: [{
        label: 'Spectrometer data',
        data: Object.values(obj[0])
      }]
    },
    options: {
      responsive: false
    }
  });
}
