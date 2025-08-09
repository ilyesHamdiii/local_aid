let nav = document.querySelector(".nav");
document.addEventListener("scroll", () => {
  console.log(window.scrollY);
  if (window.scrollY > 30) {
    nav.classList.add("scroll");
  } else {
    nav.classList.remove("scroll");
  }
});
