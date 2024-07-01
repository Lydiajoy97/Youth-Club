// From the Code Insitute walkthrough video

const editButtons = document.getElementsByClassName("btn-edit");
const suggestionText = document.getElementById("id_body");
const suggestionForm = document.getElementById("suggestionForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let suggestionId = e.target.getAttribute("suggestion_id");
    let suggestionContent = document.getElementById(`suggestion${suggestionId}`).innerText;
    suggestionText.value = suggestionContent;
    submitButton.innerText = "Update";
    suggestionForm.setAttribute("action", `edit_suggestion/${suggestionId}`);
  });
}