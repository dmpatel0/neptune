const sharpeRatio = parseFloat(document.getElementById('sharpeRatioValue').innerText);
const annualReturn = parseFloat(document.getElementById('annualReturnValue').innerText);
const volatility = parseFloat(document.getElementById('volatilityValue').innerText);
const buyHoldReturn = parseFloat(document.getElementById('buyHoldReturnValue').innerText);
const strategyReturn = parseFloat(document.getElementById('strategyReturnValue').innerText);

function updateMetricColors() {
    const sharpeRatioContainer = document.getElementById('sharpeRatioContainer');
    const annualReturnContainer = document.getElementById('annualReturnContainer');
    const volatilityContainer = document.getElementById('volatilityContainer');
    const buyHoldReturnContainer = document.getElementById('buyHoldReturnContainer');
    const strategyReturnContainer = document.getElementById('strategyReturnContainer');

    if (sharpeRatio > 0.75) {
        sharpeRatioContainer.classList.remove('default', 'red', 'yellow');
        sharpeRatioContainer.classList.add('green');
    } else if (sharpeRatio > 0.5) {
        sharpeRatioContainer.classList.remove('default', 'red', 'green');
        sharpeRatioContainer.classList.add('yellow');
    } else {
        sharpeRatioContainer.classList.remove('default', 'green', 'yellow');
        sharpeRatioContainer.classList.add('red');
    }

    if (annualReturn > 10) {
        annualReturnContainer.classList.remove('default', 'red', 'yellow');
        annualReturnContainer.classList.add('green');
    } else if (annualReturn > 0) {
        annualReturnContainer.classList.remove('default', 'red', 'green');
        annualReturnContainer.classList.add('yellow');
    } else {
        annualReturnContainer.classList.remove('default', 'green', 'yellow');
        annualReturnContainer.classList.add('red');
    }

    if (volatility < 10) {
        volatilityContainer.classList.remove('default', 'red', 'yellow');
        volatilityContainer.classList.add('green');
    } else if (volatility < 20) {
        volatilityContainer.classList.remove('default', 'red', 'green');
        volatilityContainer.classList.add('yellow');
    } else {
        volatilityContainer.classList.remove('default', 'green', 'yellow');
        volatilityContainer.classList.add('red');
    }

    if (buyHoldReturn > 10) {
        buyHoldReturnContainer.classList.remove('default', 'red', 'yellow');
        buyHoldReturnContainer.classList.add('green');
    } else if (buyHoldReturn > 0) {
        buyHoldReturnContainer.classList.remove('default', 'red', 'green');
        buyHoldReturnContainer.classList.add('yellow');
    } else {
        buyHoldReturnContainer.classList.remove('default', 'green', 'yellow');
        buyHoldReturnContainer.classList.add('red');
    }

    if (strategyReturn > 10) {
        strategyReturnContainer.classList.remove('default', 'red', 'yellow');
        strategyReturnContainer.classList.add('green');
    } else if (strategyReturn > 0) {
        strategyReturnContainer.classList.remove('default', 'red', 'green');
        strategyReturnContainer.classList.add('yellow');
    } else {
        strategyReturnContainer.classList.remove('default', 'green', 'yellow');
        strategyReturnContainer.classList.add('red');
    }

}