// basic client-side validation for the post form
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("postForm");
  if (!form) return;
  form.addEventListener("submit", (e) => {
    const title = form.querySelector('[name="title"]').value.trim();
    const desc = form.querySelector('[name="description"]').value.trim();
    if (title.length < 5 || desc.length < 10) {
      e.preventDefault();
      alert(
        "Please provide a clear title (5+ chars) and description (10+ chars)."
      );
    }
  });
});
