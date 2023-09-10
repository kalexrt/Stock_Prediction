// const url2 = "http://127.0.0.1:8000/stock/"+ "{{stock_symbol | safe}}";
// const url2 = "http://127.0.0.1:8000/stock/NABIL";
// const url2 = "http://127.0.0.1:8000/stock/";
// console.log(url2);
// document.getElementById("testObject").innerHTML = url2;


// $(document).ready(function () {
//     $.ajax({
//         url: url2,
//         type: 'GET',
//         datatype: "json",
//         success: successFunction
//     });
// });

// var dataset = [];
// function successFunction(object) {
//     var str = " ";
//     object.forEach((value, index) => {
//         var dobject = {
//             x: value.Date,
//             y: []
//         }

//         dobject.y.push(value.Open, value.Close, value.High, value.Low, value.Vol);
//         dataset.push(dobject);
//     });

//     chart.updateSeries([{
//         data: dataset
//     }])
// }

// var options = {
//     series: [],
//     chart: {
//         type: 'candlestick',
//         height: 350
//     },
//     title: {
//         text: 'CandleStick Chart',
//         align: 'left'
//     },
//     xaxis: {
//         type: 'datetime'
//     },
//     yaxis: {
//         tooltip: {
//             enabled: true
//         }
//     },
//     noData: {
//         text: 'Loading...'
//     }
// };

// var chart = new ApexCharts(document.querySelector("#chart"), options);

// chart.render();
