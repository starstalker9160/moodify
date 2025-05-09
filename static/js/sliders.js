document.addEventListener("DOMContentLoaded", function() {
    const submitBtn = document.querySelector("#submit");
    const colors = {
        happy: ["#EFE2FA", "#BACBFE", "#8F9FE4", "#BCA5D4", "#7164B4"],
        anger: ["#F7B538", "#DB7C26", "#D8572A", "#C32F27", "#780116"],
        anxiousness: ["#C8D53E", "#A3C844", "#84BE4A", "#609E43", "#3C6C3B"]
    };

    function updateBoxColor(inputId, boxIndex) {
        const input = document.getElementById(inputId);
        const boxes = document.querySelectorAll(".box");
        const value = parseInt(input.value);``
        if (value >= 1 && value <= 5) {
            boxes[boxIndex].style.backgroundColor = colors[inputId][value - 1];
        }
    }

    document.getElementById("happy").addEventListener("input", function() {
        updateBoxColor("happy", 0);
    });
    document.getElementById("anger").addEventListener("input", function() {
        updateBoxColor("anger", 1);
    });
    document.getElementById("anxiousness").addEventListener("input", function() {
        updateBoxColor("anxiousness", 2);
    });

    updateBoxColor("happy", 0);
    updateBoxColor("anger", 1);
    updateBoxColor("anxiousness", 2);


    submitBtn.addEventListener("click", function() {
        submitBtn.disabled = true;

        const happyValue = document.getElementById("happy").value;
        const angerValue = document.getElementById("anger").value;
        const anxiousnessValue = document.getElementById("anxiousness").value;

        const data = {
            happy: parseInt(happyValue),
            anger: parseInt(angerValue),
            anxiousness: parseInt(anxiousnessValue)
        };

        fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        .then(response => response.json())
        .then(data => console.log('Data received:', data))
        .catch(error => console.error('Error:', error));

        setTimeout(() => { window.location.href = '/response'; }, 2000);
    });
});
