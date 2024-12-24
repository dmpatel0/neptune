document.getElementById('submitButton').addEventListener('click', function(e) {
    e.preventDefault()
    const form = document.getElementById('backtestForm')
    const formData = new FormData(form);
    const data = {};
    
    formData.forEach((value, key) => {
        data[key] = value;
    });

    if(data['ticker'] === "" | data['sDate'] === "" | data['eDate'] === "" | data['strat'] === "") {
        console.log("Required fields empty. Doing nothing.")
        alert('Please fill in all the required fields.')
        return
    }

    fetch('/api/run_backtest', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })    
    .then(response => response.json())
    .then(result => {
        metrics = result.response

        document.getElementById('bhPercent').innerText = metrics['Buy & Hold Return [%]']
        document.getElementById('returnPercent').innerText = metrics['Return [%]']
        document.getElementById('returnAnnual').innerText = metrics['Return (Ann.) [%]']
        document.getElementById('sharpeRatio').innerText = metrics['Sharpe Ratio']
        document.getElementById('annVolatility').innerText = metrics['Volatility (Ann.) [%]']
        
        fetch('api/load_graph')
            .then(response => response.text())
            .then(data => {

                child = document.getElementById('embeddedGraph')
                if(child !== null) {
                    document.getElementById('graphContainer').removeChild(child)
                }
                console.log('test')
                var iframe = document.createElement('iframe');
                iframe.id = 'embeddedGraph'
                iframe.src = 'data:text/html;charset=utf-8,' + encodeURIComponent(data);
                iframe.style.width = '100%';
                iframe.style.height = '100%';
                iframe.style.border = 'none';

                document.getElementById('graphContainer').appendChild(iframe)
                console.log('iframe added')

            })
            .catch(error => console.error('Error loading embedded graph:', error));
        
    })
    .catch(error => console.error('Error:', error));
});
