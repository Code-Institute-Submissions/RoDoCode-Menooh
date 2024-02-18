const submitButton = document.getElementById("submitButton");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");


for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let postId = e.target.getAttribute("post_id");
        deletePostConfirm.href = `delete_post/${postId}`;
        deletePostModal.show();
    });
}