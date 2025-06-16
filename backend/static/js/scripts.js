
document.querySelector('#loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const email = document.querySelector('#email').value;
    const password = document.querySelector('#password').value;

    const response = await fetch('/auth/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
    });

    const result = await response.json();
    if (response.ok) {
        alert(result.message);  // "Login successful"
        // Redirect or update UI
    } else {
        alert(result.error);  // e.g., "Invalid credentials"
    }
});
