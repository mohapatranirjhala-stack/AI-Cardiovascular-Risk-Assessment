const sendBtn = document.getElementById("sendBtn");
const voiceBtn = document.getElementById("voiceBtn");
const questionInput = document.getElementById("question");
const chatBody = document.getElementById("chatBody");

// ==========================================================
// Send Question to AI
// ==========================================================

async function askAI() {

    const question = questionInput.value.trim();

    if (question === "")
        return;

    chatBody.innerHTML += `
        <div class="message user-message">
            ${escapeHTML(question)}
        </div>
    `;

    questionInput.value = "";

    chatBody.innerHTML += `
        <div class="message bot-message" id="typingMessage">
            🤖 Thinking...
        </div>
    `;

    chatBody.scrollTop = chatBody.scrollHeight;

    try {

        const response = await fetch("/ask", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })

        });

        const data = await response.json();

        const typingMessage =
            document.getElementById("typingMessage");

        if (typingMessage) {

            typingMessage.remove();

        }

        const answer = data.answer || 
            "Sorry, I could not generate an answer.";

        chatBody.innerHTML += `
            <div class="message bot-message">
                ${escapeHTML(answer)}
            </div>
        `;

        chatBody.scrollTop = chatBody.scrollHeight;

        // Read AI response aloud
        speakAnswer(answer);

    }

    catch (error) {

        console.error("AI Assistant Error:", error);

        const typingMessage =
            document.getElementById("typingMessage");

        if (typingMessage) {

            typingMessage.remove();

        }

        chatBody.innerHTML += `
            <div class="message bot-message">
                ❌ Sorry, the AI Health Assistant is currently unavailable.
            </div>
        `;

    }

}


// ==========================================================
// Send Button
// ==========================================================

sendBtn.addEventListener("click", askAI);


// ==========================================================
// Press Enter to Ask
// ==========================================================

questionInput.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

        event.preventDefault();

        askAI();

    }

});


// ==========================================================
// Voice Recognition
// ==========================================================

const SpeechRecognition =
    window.SpeechRecognition ||
    window.webkitSpeechRecognition;

let recognition = null;

if (SpeechRecognition) {

    recognition = new SpeechRecognition();

    recognition.continuous = false;

    recognition.interimResults = false;

    recognition.lang = "en-IN";


    recognition.onstart = function() {

        voiceBtn.innerHTML = "🔴";

        voiceBtn.title = "Listening...";

        voiceBtn.classList.add("listening");

    };


    recognition.onresult = function(event) {

        const transcript =
            event.results[0][0].transcript;

        questionInput.value = transcript;

        // Automatically send voice question
        askAI();

    };


    recognition.onerror = function(event) {

        console.error(
            "Voice recognition error:",
            event.error
        );

        voiceBtn.innerHTML = "🎤";

        voiceBtn.title = "Speak your question";

        voiceBtn.classList.remove("listening");

    };


    recognition.onend = function() {

        voiceBtn.innerHTML = "🎤";

        voiceBtn.title = "Speak your question";

        voiceBtn.classList.remove("listening");

    };


    voiceBtn.addEventListener("click", function() {

        try {

            recognition.start();

        }

        catch (error) {

            console.log(
                "Voice recognition already running."
            );

        }

    });

}

else {

    voiceBtn.disabled = true;

    voiceBtn.innerHTML = "🎤";

    voiceBtn.title =
        "Voice recognition is not supported in this browser";

}


// ==========================================================
// AI Voice Response
// ==========================================================

function speakAnswer(text) {

    if (!("speechSynthesis" in window)) {

        return;

    }

    // Stop any previous speech
    window.speechSynthesis.cancel();

    const cleanText =
        text.replace(/[*#_`]/g, "");

    const speech =
        new SpeechSynthesisUtterance(cleanText);

    speech.lang = "en-IN";

    speech.rate = 0.95;

    speech.pitch = 1;

    speech.volume = 1;

    window.speechSynthesis.speak(speech);

}


// ==========================================================
// Stop AI Voice
// ==========================================================

function stopAIVoice() {

    if ("speechSynthesis" in window) {

        window.speechSynthesis.cancel();

    }

}


// ==========================================================
// Escape HTML
// ==========================================================

function escapeHTML(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;

}