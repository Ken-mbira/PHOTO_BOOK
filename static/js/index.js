$(document).ready(function() {
    var myModal = new bootstrap.Modal(document.getElementById('gallery-modal'))
    myModal.show()
    $('.image').click(function() {
        var myModal = new bootstrap.Modal(document.getElementById('gallery-modal'))
        myModal.show()
    })
    $("#copy-link").click(function(e) {
        var message = e.target
        navigator.clipboard.writeText(message.value)
        var otherModal = new bootstrap.Modal(document.getElementById('success-modal'))
        otherModal.show()
    })
})