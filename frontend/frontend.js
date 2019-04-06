$('#update').click(updateData())
function updateData () {
  const url = 'http://' + window.location.hostname + ':5000/data';
  $.get(url, function (data, status) {
    $('#debug').text(data);
  })
}
