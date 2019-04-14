$('#update').click(updateData);
// jQuery event binder

function updateData (obj) {
  // download data from backend into obj
  const url = 'http://' + window.location.hostname + ':5000/data';
  // I understand how bad this line looks. Please don't judge me...
  $.get(url, function (data, status) { // standard jQuery AJAX
    obj = data;
  });
}

function applyData (obj, dom) {
  // applies data in obj[0] to HTML tags with the obj's key as ID.
  // useful mostly for slapping spectrometer JSON into HTML tables.
  for (var i in obj[0]) {
    $(dom).find('#' + i).text(obj[0][i]);
  }
}
