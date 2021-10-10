// $(document).ready(function() {
//     $(".image").click(function(e) {
//         const src = e.target.getAttribute('src');
//         const data = e.target.getAttribute('value');
//         const pk = e.target.getAttribute('id');
//         const data2 = JSON.parse(JSON.parse(data))
//         document.querySelector(".modal-img").src = src;
//         var myModal = new bootstrap.Modal(document.getElementById('gallery-modal'))
//         myModal.show()
//         $(".modal-title").html(data2[pk].fields.name)
//         $("#image-description").html(data2[pk].fields.descriptions)
//         $("#image-category").html(data2[pk].fields.category)
//         $("#date-taken").html(data2[pk].fields.date_taken)
//     })
// })