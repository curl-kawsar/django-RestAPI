async function registerUser() {
    const url = 'http://127.0.0.1:8000/appointment/';
    const userData = {
        username: 'testuser',
        password: 'testpassword',
        email: 'testuser@example.com',
        first_name: 'Test',
        last_name: 'User'
    };

    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Registration successful:', data);
    } catch (error) {
        console.error('There was a problem with the registration operation:', error);
    }
}

// Call the function to register a user
registerUser();