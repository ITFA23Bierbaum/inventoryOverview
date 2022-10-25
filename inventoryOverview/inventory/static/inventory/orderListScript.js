function filter(event) {
    if (event.keyCode >= 48 && event.keyCode <= 57
            || event.keyCode >= 65 && event.keyCode <= 90
            || event.keyCode == 8) {
        frm_filter.submit();
    }
}

function addFilterToOrders() {
    [].slice.call(document.getElementsByClassName('filter')[0].getElementsByTagName('input'))
            .forEach(function(e) {
        e.addEventListener('keyup', filter, false);
    });
}

function orderClick(orderNo) {
    document.getElementById('input_redirectValue').value = orderNo;
    frm_redirect.submit();
}