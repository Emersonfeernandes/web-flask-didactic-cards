let currentIndex = 0;

const card = document.querySelector(".card");
const front = document.getElementById("front");
const back = document.getElementById("back");
const nextBtn = document.getElementById("next-card");
const progressInfo = document.getElementById("progress-info");

function updateProgress() {
  if (progressInfo) {
    progressInfo.textContent = `Cartão ${currentIndex + 1} de ${questData.length}`;
  }
}

card.addEventListener("click", function () {
  this.classList.toggle("flip");
});

nextBtn.addEventListener("click", function () {
  currentIndex++;
  if (currentIndex >= questData.length) {
    currentIndex = 0;
  }

  card.classList.remove("flip");

  setTimeout(() => {
    front.querySelector(".card-text").textContent = questData[currentIndex][0];
    back.querySelector(".card-text").textContent = questData[currentIndex][1];
    updateProgress();
  }, 350);
});

updateProgress();