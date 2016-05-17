$(document).ready(function() {

  $('#datetimepicker1').datetimepicker({
    format: 'YYYY-MM-DD',
    // useCurrent: true
  });

  $.get('/positions', {accountId: 1, date: 1, stats: 1})
    .done(function(stats) {
      $('#marketValue').text(stats.marketValue);
    });
  $.get('/positions', {accountId: 1, date: 1})
    .done(function(rawData) {
      try {
        let jsonData = JSON.parse(rawData);
        let columns = jsonData.columns.map(function(val) {
          return {
            field: val,
            title: val
          }
        });
        columns.unshift({field: 'id', title: 'id'});
        let data = jsonData.data.map(function(dataRow, indexRow) {
          let tempObj = {id: indexRow};
          for (let i=0; i<dataRow.length; i++) {
            tempObj[jsonData.columns[i]] = dataRow[i];
          }
          return tempObj;
        });

        $('#table').bootstrapTable({
          columns: columns,
          data: data
        });


      } catch(e) {
        console.log('Error while parsing json data', e);
      }
    });
  $('#dropdownAccounts .dropdown-menu li a').on('click', function(e) {
    $('#dropdownAccounts button .dropdown-title').text(this.innerText);
  });

});
