const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let cookbookId = e.target.getAttribute("cookbook_id");
        deleteConfirm.href = `delete_cookbook/${cookbookId}`;
        deleteModal.show();
    });
}