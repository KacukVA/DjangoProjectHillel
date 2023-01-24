$('.delete').click(function () {
    $(this).parent().remove()
    $.ajax({
        url: `/api/groups/${$(this).siblings('p').data('groupId')}`, type: 'DELETE', success: function (result) {
            console.log(result)
        }
    })
})

$('.update').click(function () {
    let data = {
        'id': $(this).siblings('p').data('groupId'), 'name': $(this).siblings('p').text().trim(),
    }
    $.ajax({
        url: `/api/groups/${$(this).siblings('p').data('groupId')}/`, type: 'PUT', data, success: function (result) {
            console.log(result)
        }
    })
})

$('#create').click(function () {
    let data = {
        'name': 'new group',
    }
    $.ajax({
        url: `/api/groups/`, type: 'POST', data, success: function (result) {
            $('#groups').append(`<tr><td><p contentEditable="true" data-group-id="${result.id}">new group</p><button type="button" class="btn btn-success update">Update</button><button type="button" class="btn btn-danger delete">Delete</button></td></tr>`)
        }
    })
})

$('#get').click(function () {
    $.ajax({
        url: `/api/groups/`, type: 'GET', success: function (result) {
            console.log(result)
        }
    })
})
