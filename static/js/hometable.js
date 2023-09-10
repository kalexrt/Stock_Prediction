
const matchDoubleQuotesRegex = /(?:")(?=(?:[^"]|"[^]*")*$)/g;
const matchNewLine = /\r?\n|\r/;




function table(url_value, div_id) {
    $.ajax({
        url: url_value,
        dataType: "text",
        success: function (data) {
            //var stock_data = data.split(/\r?\n|\r/); 
            var stock_data = data.split(/(?<=^[^"]*(?:"[^"]*"[^"]*)*)\r?\n/);
            var table_data = '<table class="table table-bordered table-striped">';
            for (var count = 0; count < stock_data.length; count++) {
                var cell_data = stock_data[count].split(",");
                table_data += '<tr>';
                for (var cell_count = 0; cell_count < cell_data.length; cell_count++) {
                    if (count === 0) {
                        table_data += '<th>' + cell_data[cell_count] + '</th>';
                    }
                    else {
                        table_data += '<td>' + cell_data[cell_count] + '</td>';
                    }
                }
                table_data += '</tr>';
            }
            table_data += '</table>';
            $('#' + div_id).html(table_data);
        }
    });

}


$(document).ready(loop);

function loop() {
    for (var i = 1; i <= 6; i++) {
        url_csv = "../static/csv/stock" + i + ".csv";
        stock_div = "stock_table" + i;
        table(url_csv, stock_div);
    }
}