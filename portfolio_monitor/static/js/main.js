$(document).ready(function() {

  $('#datetimepicker1').datetimepicker({
    format: 'YYYY-MM-DD',
    // useCurrent: true
  });

  $('#dropdownAccounts .dropdown-menu li a').on('click', function(e) {
    $('#dropdownAccounts button .dropdown-title').text(this.innerText);
  });

  var getStats = function(options) {
    $.get('/positions', {accountId: 1, date: 1, stats: 1})
      .done(function(stats) {
        $('#marketValue').text(stats.marketValue);
      });
  };
  var getPosition = function(options) {
    $.get('/positions', {accountId: 1, date: 1})
    .done(function(rawData) {
      try {
        var jsonData = JSON.parse(rawData);
        var columns = jsonData.columns.map(function(val) {
          return {
            field: val,
            title: val
          }
        });
        columns.unshift({field: 'id', title: 'id'});
        var data = jsonData.data.map(function(dataRow, indexRow) {
          var tempObj = {id: indexRow};
          for (var i=0; i<dataRow.length; i++) {
            tempObj[jsonData.columns[i]] = dataRow[i];
          }
          return tempObj;
        });

        if (typeof(options) === 'object' && options.refresh) {
          $('#table').bootstrapTable('load', {
            columns: columns,
            data: data,
            silent: true
          });
        } else {
          $('#table').bootstrapTable({
            columns: columns,
            data: data
          });
        }


      } catch(e) {
        console.log('Error while parsing json data', e);
      }
    });
  };

  getStats();
  getPosition();
  // Refresh data
  var interval = 2 * 1000;
  setInterval(function() {
    getStats({accountId: 1, date: 1, refresh: true});
    getPosition({accountId: 1, date: 1, refresh: true});
  }, interval);

});
