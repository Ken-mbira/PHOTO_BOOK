$(document).ready(function() {
    $(".image").click(function(e) {
        const src = e.target.getAttribute('src');
        document.querySelector(".modal-img").src = src;
        var myModal = new bootstrap.Modal(document.getElementById('gallery-modal'))
        myModal.show()
    })
})