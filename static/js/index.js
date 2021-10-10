$(document).ready(function() {
    $(".image").click(function(e) {
        var myModal = new bootstrap.Modal(document.getElementById('gallery-modal'))
        myModal.show()
    })
})