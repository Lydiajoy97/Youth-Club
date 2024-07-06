// From the Code Insitute walkthrough video

// const editButtons = document.getElementsByClassName("btn-edit");
// const activityText = document.getElementById("id_body");
// const activityForm = document.getElementById("activityForm");
// const submitButton = document.getElementById("submitButton");

// for (let button of editButtons) {
//   button.addEventListener("click", (e) => {
//     let activityId = e.target.getAttribute("activityForm_id");
//     let activityContent = document.getElementById(`activityForm${activityId}`).innerText;
//     activityText.value = activityContent;
//     submitButton.innerText = "Update";
//     activityForm.setAttribute("action", `edit_activity/${activityId}`);
//   });
// }