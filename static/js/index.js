$(document).ready(function() {
    var myModal = new bootstrap.Modal(document.getElementById('gallery-modal'))
    myModal.show()
    $('.image').click(function() {
        var myModal = new bootstrap.Modal(document.getElementById('gallery-modal'))
        myModal.show()
    })
})