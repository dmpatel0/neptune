document.getElementById('login-button').addEventListener('click', function(e) {
    e.preventDefault();
    const form = document.getElementById('login-form');
    const formData = new FormData(form);
    const data = {};

    formData.forEach((value, key) => {
        data[key] = value;
    });

    if(data['username'] === "" | data['password'] === "") {
        console.log("Required fields empty. Doing nothing.")
        alert('Please fill in all the required fields.')
        return
    }

    fetch('api/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(result => {

        message = result.response

        alert(message)
    })
    .catch(error => console.error('Error:', error));
})