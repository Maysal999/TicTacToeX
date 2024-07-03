
document.addEventListener("DOMContentLoaded", function() {
    const cells = document.querySelectorAll(".cell");
    const statusDisplay = document.getElementById("game-status");
    const restartButton = document.getElementById("restart-game");
    const user = "{{ user.username }}"; // Имя пользователя для отправки данных

    let board = ["", "", "", "", "", "", "", "", ""];
    let currentPlayer = "X";
    let gameActive = true;

    const winningConditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ];

    function handleCellPlayed(clickedCell, clickedCellIndex) {
        board[clickedCellIndex] = currentPlayer;
        clickedCell.innerHTML = currentPlayer;
    }

    function handleResultValidation() {
        let roundWon = false;
        for (let i = 0; i < winningConditions.length; i++) {
            const winCondition = winningConditions[i];
            let a = board[winCondition[0]];
            let b = board[winCondition[1]];
            let c = board[winCondition[2]];
            if (a === "" || b === "" || c === "") {
                continue;
            }
            if (a === b && b === c) {
                roundWon = true;
                break;
            }
        }

        if (roundWon) {
            statusDisplay.innerHTML = `Игрок ${currentPlayer} выиграл!`;
            gameActive = false;
            saveGameResult(currentPlayer);
            return;
        }

        let roundDraw = !board.includes("");
        if (roundDraw) {
            statusDisplay.innerHTML = "Ничья!";
            gameActive = false;
            saveGameResult(null);
            return;
        }

        currentPlayer = currentPlayer === "X" ? "O" : "X";
        if (currentPlayer === "O") {
            botMove();
        }
    }

    function botMove() {
        let availableCells = [];
        board.forEach((cell, index) => {
            if (cell === "") availableCells.push(index);
        });

        if (availableCells.length === 0) return;

        let randomIndex = Math.floor(Math.random() * availableCells.length);
        let botMoveIndex = availableCells[randomIndex];
        let botCell = document.getElementById(`cell-${botMoveIndex}`);

        handleCellPlayed(botCell, botMoveIndex);
        handleResultValidation();
    }

    function handleCellClick(clickedCellEvent) {
        const clickedCell = clickedCellEvent.target;
        const clickedCellIndex = parseInt(clickedCell.getAttribute("id").split("-")[1]);

        if (board[clickedCellIndex] !== "" || !gameActive) {
            return;
        }

        handleCellPlayed(clickedCell, clickedCellIndex);
        handleResultValidation();
    }

    function handleRestartGame() {
        gameActive = true;
        currentPlayer = "X";
        board = ["", "", "", "", "", "", "", "", ""];
        statusDisplay.innerHTML = "";
        cells.forEach(cell => cell.innerHTML = "");
    }

    function saveGameResult(winner) {
        fetch("/save_game_result/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": "{{ csrf_token }}"
            },
            body: JSON.stringify({
                player1: user,
                player2: "Bot",
                winner: winner,
                against_bot: true
            })
        });
    }

    cells.forEach(cell => cell.addEventListener("click", handleCellClick));
    restartButton.addEventListener("click", handleRestartGame);
});