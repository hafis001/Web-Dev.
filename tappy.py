<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TappyCoin</title>
    <style>
        .button {
            padding: 10px 20px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="game">
        <h1>Button Game</h1>
        <p>Points: <span id="points">0</span></p>
        <p>Level: <span id="level">1</span></p>
        <button class="button" onclick="clickButton()">Click Me</button>
    </div>
    <script>
        var points = localStorage.getItem("points") ? parseInt(localStorage.getItem("points")) : 0;
        var level = localStorage.getItem("level") ? parseInt(localStorage.getItem("level")) : 1;

        updateDisplay();

        function clickButton() {
            points++;
            updateDisplay();
            localStorage.setItem("points", points);
            if (points >= level * 1000) {
                levelUp();
            }
        }

        function levelUp() {
            level++;
            updateDisplay();
            localStorage.setItem("level", level);
            alert("Congratulations! You reached level " + level);
        }

        function updateDisplay() {
            document.getElementById("points").innerText = points;
            document.getElementById("level").innerText = level;
        }

        function main() {
            while (true) {
                var choice = prompt("Press 'c' to click the button or 'q' to quit.").toLowerCase();
                if (choice === 'c') {
                    clickButton();
                } else if (choice === 'q') {
                    alert("Game over. Final points: " + points);
                    break;
                } else {
                    alert("Invalid choice. Please try again.");
                }
            }
        }

        main(); // Call main function when the page loads
    </script>
</body>
</html>
