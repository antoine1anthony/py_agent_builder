const projectData = {
    project_name: "Calculator app",
    project_description: "Make a calculator app that uses tensorflow",
    selected_bot_names: ["Mx.Pythonista", "Mx.ReactNative"],
    bot_name: "Mx.Pythonista",  // Specify which bot should take the turn
    user_message: "I want to create a calculator app using TensorFlow. Any advice?"  // The message from the user
};

fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(projectData)
})
.then(response => response.json())
.then(data => {
    console.log(data);  // This will log the response from the bot
})
.catch((error) => {
    console.error('Error:', error);
});
