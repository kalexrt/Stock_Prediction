window.addEventListener('load', setup);

async function setup() {
    const ctx = document.getElementById('myChart').getContext('2d');
    const globalstock_price = await getData();
    const myChart1 = new Chart(ctx, {
        type: 'line',
        data: {
            labels: globalstock_price.time_label,
            datasets: [{
                label: 'Stock Price',
                data: globalstock_price.stock_price,
                fill: false,
                borderColor: 'rgba(255, 99, 132, 1)',
                backgroundColor: 'rgba(255, 99, 132, 0.5)',
                borderWidth: 1
            }]
        },
        options: {}
    });
}

async function getData() {
    // const response = await fetch('testdata.csv');
    const response = await fetch('../static/csv/stock.csv');
    const data = await response.text();
    const time_label = [];
    const stock_price = [];
    const rows = data.split('\n').slice(1);
    rows.forEach(row => {
        const cols = row.split(',');
        time_label.push(cols[0]);
        stock_price.push(cols[1]);
    });
    return {
        time_label,
        stock_price
    };
}
