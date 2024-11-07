let score = 0;
let timeLeft = 30;
const namesContainer = document.getElementById('names-container');
const ingredientsContainer = document.getElementById('ingredients-container');
const checkButton = document.getElementById('check-button');
const resultDisplay = document.getElementById('result');
const scoreDisplay = document.getElementById('score');
const timerDisplay = document.getElementById('timer');
const playAgainButton = document.getElementById('play-again');
let timerInterval = null;
function startTimer() {
    timeLeft = 30;
    timerDisplay.textContent = "Time Left: "+timeLeft.toString();
    timerInterval = setInterval(() => {
        scoreDisplay.textContent = `Score: ${score}`;
        
        timerDisplay.textContent = "Time Left: "+timeLeft.toString();
        if (timeLeft <= 0) {
            
            timeLeft=0;
            endGame("Time's up!");
            return;
        }else{
            timeLeft--;
        }
    }, 1000);
}

function getFoods(){
    fetch('/get_foods')
    .then(response => response.json())
    .then(data => {
        startTimer()
        data.foods.forEach((data, index) => {
            const nameDiv = document.createElement('div');
            nameDiv.textContent = data.name;
            nameDiv.className = 'draggable';
            nameDiv.draggable = true;
            nameDiv.id = `${data.id}`;
            namesContainer.appendChild(nameDiv);
            nameDiv.addEventListener('dragstart', (e) => {
                e.dataTransfer.setData('text/plain', nameDiv.id); 
            });
            const ingredientDiv = document.createElement('div');
            ingredientDiv.dataset.fullIngredients = JSON.stringify(data.ingredients);
            let displayText = data.ingredients.join(", "); // Properly join the ingredients
            displayText = displayText.length > 50 ? displayText.slice(0, 50) + "..." : displayText;
            ingredientDiv.textContent = displayText;
          
          
              ingredientDiv.addEventListener('mouseover', function () {
                  const fullIngredients = JSON.parse(this.dataset.fullIngredients);
                  let tooltipText = fullIngredients.join(", ");
          
                  // Create the tooltip element if it doesn't exist
                  let tooltip = document.getElementById('tooltip-' + this.id);
                  if (!tooltip) {
                      tooltip = document.createElement('div');
                      tooltip.id = 'tooltip-' + this.id;
                      tooltip.classList.add('tooltip');
                      document.body.appendChild(tooltip);
                  }
          
                  tooltip.style.top = (this.offsetTop + this.offsetHeight) + 'px';
                  tooltip.style.left = this.offsetLeft + 'px';
                  tooltip.style.display = 'block';
                  tooltip.textContent = tooltipText;
                  
              });
          
            ingredientDiv.addEventListener('mouseout', function () {
                  const tooltip = document.getElementById('tooltip-' + this.id);
                  if (tooltip) {
                    tooltip.style.display = 'none';
                  }
              });
            ingredientDiv.textContent = data.ingredients;
            ingredientDiv.className = 'droppable';
            ingredientDiv.id = `ingredients-${data.id}`;
            ingredientsContainer.appendChild(ingredientDiv);
        })
    });
}

function cheekAws(){
    let correctCount = 0;
    const ingredients = document.getElementsByClassName('droppable');
    for(let i = 0; i < ingredients.length; i++) {
        const ingredientDiv = ingredients[i];
        const droppedNameDiv = ingredientDiv.querySelector('.draggable'); 

        if (droppedNameDiv) {
            const droppedNameID = droppedNameDiv.id;
            const ingredientID = ingredientDiv.id.split('-')[1];

            if (ingredientID === droppedNameID) {
                correctCount++;
            }
        }
    }
    score = correctCount * (timeLeft);
    scoreDisplay.textContent = `Score: ${score}`;
    resultDisplay.textContent = `You got ${correctCount} out of ${ingredients.length} correct!  Final Score: ${score}`;
}

function makeDragable(){
    const nameElements = document.querySelectorAll('.draggable');
    nameElements.forEach(element => {
        element.draggable = true;
        element.style.cursor = 'default'; 
        element.style.opacity = '1'
    });

    ingredientsContainer.addEventListener('dragover', (e) => {
        e.preventDefault();
    });
    ingredientsContainer.addEventListener('drop', (e) => {
        e.preventDefault();
        const draggedId = e.dataTransfer.getData('text/plain');
        const draggedElement = document.getElementById(draggedId);
        let targetDiv = e.target.closest('.droppable');
        if (targetDiv) {
            if (draggedElement.parentElement === targetDiv) {
                return
            }
            if (targetDiv.querySelector('.draggable')) {
                namesContainer.appendChild(targetDiv.querySelector('.draggable'));
            }
            targetDiv.appendChild(draggedElement);
        } else {
            if (draggedElement.parentElement === namesContainer) {
                return
            }
            namesContainer.appendChild(draggedElement);
        }
    });

    namesContainer.addEventListener('dragover', (e) => {
        e.preventDefault();
    });
    
    namesContainer.addEventListener('drop', (e) => {
    
        e.preventDefault();
        const draggedId = e.dataTransfer.getData('text/plain');
        const draggedElement = document.getElementById(draggedId);
        if (draggedElement.parentElement === namesContainer) { 
            return
        }
        namesContainer.appendChild(draggedElement);
    
    });
}

function makeUndraggable() {
    const nameElements = document.querySelectorAll('.draggable');
    nameElements.forEach(element => {
        element.draggable = false;
        element.style.cursor = 'default'; 
        element.style.opacity = '0.5'

    });
}

function endGame (){
    clearInterval(timerInterval);
    cheekAws();
    makeUndraggable();
    checkButton.disabled = true;
    playAgainButton.style.display = 'block';
    document.getElementById('result-container').style.display = 'flex';
}

checkButton.addEventListener('click', endGame);
playAgainButton.addEventListener('click', play);

function play(){
    document.getElementById('result-container').style.display = 'none';
    namesContainer.innerHTML = '';
    ingredientsContainer.innerHTML = '';
    resultDisplay.textContent = '';
    playAgainButton.style.display = 'none';
    getFoods();
    makeDragable();
    checkButton.disabled = false;
}


document.addEventListener('DOMContentLoaded', play);