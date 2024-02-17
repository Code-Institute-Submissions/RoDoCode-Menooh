const editButtons = document.getElementsByClassName("btn-edit");
const cookbookText = document.getElementById("id_body");
const cookbookForm = document.getElementById("cookbookForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let cookbookId = e.target.getAttribute("cookbook_id");
        let cookbookContent = document.getElementById(`cookbook${cookbookId}`).innerText;
        cookbookText.value = cookbookContent;
        submitButton.innerText = "Update";
        cookbookForm.setAttribute("action", `edit_cookbook/${cookbookId}`);
    });
}


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let cookbookId = e.target.getAttribute("cookbook_id");
        deleteConfirm.href = `delete_cookbook/${cookbookId}`;
        deleteModal.show();
    });
}