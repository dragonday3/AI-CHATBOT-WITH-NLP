document.getElementById("send-button").onclick = function() {
    const userInput = document.getElementById("user-input").value;
    if (userInput) {
        addMessage("You: " + userInput);
        document.getElementById("user-input").value = "";

        fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            addMessage(" Chatbot: " + data.response);
        });
    }
};

function addMessage(message) {
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += message + "<br/><br/>";
    chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
}
