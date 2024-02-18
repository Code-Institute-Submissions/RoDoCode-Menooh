const deletePostModal = new bootstrap.Modal(document.getElementById("deletePostModal"));
const deletePostButtons = document.getElementsByClassName("post-kill");
const deletePostConfirm = document.getElementById("deletePostConfirm");


for (let button of deletePostButtons) {
    button.addEventListener("click", (e) => {
        console.log("bum");
        let postId = e.target.getAttribute("post_id");
        deletePostConfirm.href = `post_delete/${postId}`;
        deletePostModal.show();
    });
}